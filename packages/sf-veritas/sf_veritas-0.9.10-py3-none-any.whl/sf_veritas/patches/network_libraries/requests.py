"""
Monkey-patch the `requests` stack (requests → urllib3 → http.client):

• For every outbound request, propagate the SAILFISH_TRACING_HEADER
  unless the destination host is in `domains_to_not_propagate_headers_to`.
• Fire NetworkRequestTransmitter via utils.record_network_request
  so we always capture (url, status, timings, success, error).
"""

from __future__ import annotations

import http.client
import time
from typing import Dict, List, Optional, Tuple

import requests
import urllib3
from requests.sessions import Session

from ...constants import SAILFISH_TRACING_HEADER
from ...thread_local import (
    activate_reentrancy_guards_exception,
    activate_reentrancy_guards_logging,
    activate_reentrancy_guards_print,
)
from .utils import get_trace_and_should_propagate, record_network_request

###############################################################################
# Internal helpers
###############################################################################

# header names used for re-entrancy guards
REENTRANCY_GUARD_LOGGING_PREACTIVE = "reentrancy_guard_logging_preactive"
REENTRANCY_GUARD_PRINT_PREACTIVE = "reentrancy_guard_print_preactive"
REENTRANCY_GUARD_EXCEPTIONS_PREACTIVE = "reentrancy_guard_exception_preactive"


def _activate_rg(headers: Dict[str, str]) -> None:
    """Turn the three ‘preactive' guard flags ON for downstream hops."""
    headers[REENTRANCY_GUARD_LOGGING_PREACTIVE] = "true"
    headers[REENTRANCY_GUARD_PRINT_PREACTIVE] = "true"
    headers[REENTRANCY_GUARD_EXCEPTIONS_PREACTIVE] = "true"


def _check_rg(headers: Dict[str, str]) -> None:
    """If any pre-active guard present, switch the corresponding guard on."""
    if headers.get(REENTRANCY_GUARD_LOGGING_PREACTIVE, "false").lower() == "true":
        activate_reentrancy_guards_logging()
    if headers.get(REENTRANCY_GUARD_PRINT_PREACTIVE, "false").lower() == "true":
        activate_reentrancy_guards_print()
    if headers.get(REENTRANCY_GUARD_EXCEPTIONS_PREACTIVE, "false").lower() == "true":
        activate_reentrancy_guards_exception()


def _prepare(
    url: str,
    domains_to_skip: List[str],
    headers: Optional[Dict[str, str]],
) -> Tuple[str, Dict[str, str], int]:
    """
    Inject the trace header (unless excluded) and return:
        trace_id, merged_headers, timestamp_ms
    """
    trace_id, propagate = get_trace_and_should_propagate(url, domains_to_skip)
    hdrs: Dict[str, str] = dict(headers or {})
    _check_rg(hdrs)
    if propagate:
        hdrs[SAILFISH_TRACING_HEADER] = trace_id
    _activate_rg(hdrs)
    return trace_id, hdrs, int(time.time() * 1_000)


###############################################################################
# Top-level patch function
###############################################################################
def patch_requests(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    """Apply all monkey-patches.  Safe to call multiple times."""
    exclude = domains_to_not_propagate_headers_to or []

    # --------------------------------------------------------------------- #
    # 1. Patch `requests.Session.request`
    # --------------------------------------------------------------------- #
    original_request = Session.request

    def patched_request(self: Session, method, url, **kwargs):  # type: ignore[override]
        # --- header handling / injection --------------------------------- #
        trace_id, hdrs, t0 = _prepare(url, exclude, kwargs.pop("headers", {}))
        kwargs["headers"] = hdrs

        status: int = 0
        success: bool = False
        err: str | None = None
        try:
            resp = original_request(self, method, url, **kwargs)
            status = resp.status_code
            success = resp.ok
            return resp
        except Exception as exc:  # noqa: BLE001
            err = str(exc)[:255]
            raise
        finally:
            record_network_request(
                trace_id,
                url,
                str(method).upper(),
                status,
                success,
                err,
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )

    Session.request = patched_request
    requests.Session.request = patched_request  # cover direct `requests.Session(...)`

    # --------------------------------------------------------------------- #
    # 2. Patch urllib3's low-level ConnectionPool.urlopen (used by requests)
    # --------------------------------------------------------------------- #
    original_urlopen = urllib3.connectionpool.HTTPConnectionPool.urlopen

    def patched_urlopen(self, method, url, body=None, headers=None, **kw):  # type: ignore[override]
        trace_id, hdrs, t0 = _prepare(url, exclude, headers)
        status: int = 0
        success: bool = False
        err: str | None = None
        try:
            resp = original_urlopen(self, method, url, body=body, headers=hdrs, **kw)
            status = getattr(resp, "status", 0)
            success = status < 400
            return resp
        except Exception as exc:  # noqa: BLE001
            err = str(exc)[:255]
            raise
        finally:
            record_network_request(
                trace_id,
                url,
                str(method).upper(),
                status,
                success,
                err,
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )

    urllib3.connectionpool.HTTPConnectionPool.urlopen = patched_urlopen

    # --------------------------------------------------------------------- #
    # 3. Patch http.client for “raw” stdlib usage (rare but easy to support)
    # --------------------------------------------------------------------- #
    original_http_client_request = http.client.HTTPConnection.request

    def patched_http_request(self, method, url, body=None, headers=None, *, encode_chunked=False):  # type: ignore[override]
        trace_id, hdrs, t0 = _prepare(url, exclude, headers)
        status: int = 0
        success: bool = False
        err: str | None = None
        try:
            resp = original_http_client_request(
                self,
                method,
                url,
                body=body,
                headers=hdrs,
                encode_chunked=encode_chunked,
            )
            status = getattr(
                self, "response", getattr(resp, "status", 0)
            )  # best-effort
            success = bool(status) and status < 400
            return resp
        except Exception as exc:  # noqa: BLE001
            err = str(exc)[:255]
            raise
        finally:
            record_network_request(
                trace_id,
                url,
                str(method).upper(),
                status,
                success,
                err,
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )

    http.client.HTTPConnection.request = patched_http_request
