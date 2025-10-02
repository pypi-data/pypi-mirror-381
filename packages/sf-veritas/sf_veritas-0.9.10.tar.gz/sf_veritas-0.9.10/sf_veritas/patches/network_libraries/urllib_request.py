"""
Instrument urllib.request so that

• Every call to urlopen() or OpenerDirector.open() propagates
  SAILFISH_TRACING_HEADER (unless destination host is excluded).
• Every call triggers record_network_request(…).

The patch is safe to import multiple times.
"""

from __future__ import annotations

import time
from typing import List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from .utils import get_trace_and_should_propagate, record_network_request


def patch_urllib_request(
    domains_to_not_propagate_headers_to: Optional[List[str]] = None,
) -> None:
    try:
        import urllib.error
        import urllib.request as _ur
        from urllib.parse import urlparse
    except ImportError:  # extremely unlikely
        return

    exclude: List[str] = domains_to_not_propagate_headers_to or []
    _orig_urlopen = _ur.urlopen
    _orig_opener_open = _ur.OpenerDirector.open  # type: ignore[attr-defined]

    # ------------------------------------------------------------------ #
    # Helper shared by urlopen / OpenerDirector.open
    # ------------------------------------------------------------------ #
    def _inject_and_record(
        opener_call,  # either _orig_urlopen or _orig_opener_open(self, ...)
        req_or_url,
        data,
        timeout,
        *args,
        **kwargs,
    ):
        # 1. Build a Request object
        if isinstance(req_or_url, _ur.Request):
            req = req_or_url  # already a Request
        else:
            req = _ur.Request(req_or_url, data=data)

        # Method (GET/POST/…) is resolved only *after* data & method props
        method = req.get_method()

        # 2. Header propagation decision
        trace_id, allow = get_trace_and_should_propagate(req.full_url, exclude)
        if allow:
            req.add_header(SAILFISH_TRACING_HEADER, trace_id)

        # 3. Perform the real I/O
        t0 = int(time.time() * 1_000)
        try:
            resp = opener_call(req, timeout=timeout, *args, **kwargs)
            status = (
                getattr(resp, "status", None) or getattr(resp, "getcode", lambda: 0)()
            )
            success = status < 400
            record_network_request(
                trace_id,
                req.full_url,
                method,
                status,
                success,
                None,
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )
            return resp

        except urllib.error.HTTPError as e:
            record_network_request(
                trace_id,
                req.full_url,
                method,
                e.code,
                False,
                str(e),
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )
            raise

        except Exception as e:  # noqa: BLE001
            record_network_request(
                trace_id,
                req.full_url,
                method,
                0,
                False,
                str(e)[:255],
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )
            raise

    # ------------------------------------------------------------------ #
    # Module-level urlopen patch
    # ------------------------------------------------------------------ #
    def patched_urlopen(url, data=None, timeout=_ur.socket._GLOBAL_DEFAULT_TIMEOUT, *a, **kw):  # type: ignore
        return _inject_and_record(_orig_urlopen, url, data, timeout, *a, **kw)

    _ur.urlopen = patched_urlopen  # type: ignore[assignment]

    # ------------------------------------------------------------------ #
    # OpenerDirector.open patch (covers build_opener, install_opener, etc.)
    # ------------------------------------------------------------------ #
    def patched_opener_open(self, fullurl, data=None, timeout=None, *a, **kw):  # type: ignore[override]
        # self is the OpenerDirector instance
        return _inject_and_record(
            lambda req, timeout=None, *aa, **kk: _orig_opener_open(  # bind self
                self, req, data=data, timeout=timeout, *aa, **kk
            ),
            fullurl,
            data,
            timeout,
            *a,
            **kw,
        )

    _ur.OpenerDirector.open = patched_opener_open  # type: ignore[assignment]
