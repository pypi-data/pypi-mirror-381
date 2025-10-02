"""
Monkey-patch Tornado's HTTP clients so that

• Every outbound request carries SAILFISH_TRACING_HEADER
  (unless the destination host is excluded).
• Every request – success or failure – triggers record_network_request(…).

Covers
  • tornado.httpclient.AsyncHTTPClient.fetch   (await-able)
  • tornado.httpclient.HTTPClient.fetch        (blocking/sync)
Safe to call repeatedly; patches only once per process.
"""

from __future__ import annotations

import time
from typing import List, Optional, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from .utils import get_trace_and_should_propagate, record_network_request


def patch_tornado(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    try:
        # Tornado is optional; exit silently if missing
        from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPRequest
    except ImportError:
        return

    exclude: List[str] = domains_to_not_propagate_headers_to or []

    # ------------------------------------------------------------------ #
    # Helpers shared by sync & async wrappers
    # ------------------------------------------------------------------ #
    def _resolve(
        req_or_url, kwargs
    ) -> Tuple[str, str, dict]:  # → (url, METHOD, headers_dict)
        """
        Handle both call styles:

            client.fetch("https://foo", method="POST", headers={...})
            client.fetch(HTTPRequest(...))

        Always returns a mutable *headers* dict.
        """
        if isinstance(req_or_url, HTTPRequest):
            url = req_or_url.url
            method = (req_or_url.method or "GET").upper()
            hdrs = dict(req_or_url.headers or {})
        else:
            url = str(req_or_url)
            method = kwargs.get("method", "GET").upper()
            hdrs = dict(kwargs.get("headers", {}) or {})
        return url, method, hdrs

    def _inject(
        req_or_url, kwargs, hdrs: dict
    ):  # mutate request object *or* kwargs to carry hdrs
        from tornado.httpclient import HTTPRequest  # local import to avoid MRO issues

        if isinstance(req_or_url, HTTPRequest):
            req_or_url.headers = hdrs
        else:
            kwargs["headers"] = hdrs
        return req_or_url, kwargs

    def _prepare(url: str, hdrs: dict):
        """Return (trace_id, merged_headers, start_ms)."""
        trace_id, allow = get_trace_and_should_propagate(url, exclude)
        out = dict(hdrs)
        if allow:
            out[SAILFISH_TRACING_HEADER] = trace_id
        return trace_id, out, int(time.time() * 1_000)

    # ------------------------------------------------------------------ #
    # AsyncHTTPClient.fetch wrapper
    # ------------------------------------------------------------------ #
    original_async_fetch = AsyncHTTPClient.fetch

    async def patched_async_fetch(self, req_or_url, *args, **kwargs):
        url, method, hdrs_cur = _resolve(req_or_url, kwargs)
        trace_id, hdrs_new, t0 = _prepare(url, hdrs_cur)
        req_or_url, kwargs = _inject(req_or_url, kwargs, hdrs_new)

        status, success, err = 0, False, None
        try:
            resp = await original_async_fetch(self, req_or_url, *args, **kwargs)
            status = getattr(resp, "code", 0)
            success = status < 400
            return resp
        except Exception as exc:  # noqa: BLE001
            err = str(exc)[:255]
            raise
        finally:
            record_network_request(
                trace_id,
                url,
                method,
                status,
                success,
                err,
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )

    AsyncHTTPClient.fetch = patched_async_fetch  # type: ignore[assignment]

    # ------------------------------------------------------------------ #
    # HTTPClient.fetch wrapper (blocking)
    # ------------------------------------------------------------------ #
    original_sync_fetch = HTTPClient.fetch

    def patched_sync_fetch(self, req_or_url, *args, **kwargs):
        url, method, hdrs_cur = _resolve(req_or_url, kwargs)
        trace_id, hdrs_new, t0 = _prepare(url, hdrs_cur)
        req_or_url, kwargs = _inject(req_or_url, kwargs, hdrs_new)

        status, success, err = 0, False, None
        try:
            resp = original_sync_fetch(self, req_or_url, *args, **kwargs)
            status = getattr(resp, "code", 0)
            success = status < 400
            return resp
        except Exception as exc:  # noqa: BLE001
            err = str(exc)[:255]
            raise
        finally:
            record_network_request(
                trace_id,
                url,
                method,
                status,
                success,
                err,
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )

    HTTPClient.fetch = patched_sync_fetch  # type: ignore[assignment]
