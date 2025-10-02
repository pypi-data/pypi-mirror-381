"""
Monkey-patch Niquests so that every flavour of request
(sync / async, Session / AsyncSession, streaming or not)
propagates the SAILFISH_TRACING_HEADER *and* records the request.
"""

from __future__ import annotations

import time
from typing import List, Optional, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from ..constants import supported_network_verbs as verbs
from .utils import get_trace_and_should_propagate, record_network_request


def patch_niquests(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    try:
        import niquests  # type: ignore
    except ImportError:
        return

    skip = domains_to_not_propagate_headers_to or []

    # --------------------------------------------------------------------- helpers
    SessionCls = niquests.Session
    AsyncSessionCls = getattr(niquests, "AsyncSession", type("._Dummy", (), {}))

    def _is_session_self(args: Tuple) -> bool:
        """True when args[0] is a Session/AsyncSession instance."""
        return bool(args) and isinstance(args[0], (SessionCls, AsyncSessionCls))

    def _resolve_method_url(
        verb_tag: str, args: Tuple, kwargs: dict
    ) -> Tuple[str, str]:
        """
        Robust extraction of (method, url) for every call style.
        Never throws IndexError – falls back to kwargs when positional args missing.
        """
        # ----- 1. REQUEST / AREQUEST (generic entry-points) ----------------
        if verb_tag in ("REQUEST", "AREQUEST"):
            if _is_session_self(args):
                method = (
                    str(args[1]).upper()
                    if len(args) > 1
                    else str(kwargs.get("method", "GET")).upper()
                )
                url = args[2] if len(args) > 2 else kwargs.get("url", "")
            else:
                method = (
                    str(args[0]).upper()
                    if len(args) > 0
                    else str(kwargs.get("method", "GET")).upper()
                )
                url = args[1] if len(args) > 1 else kwargs.get("url", "")

        # ----- 2. Convenience verbs get/post/… and their async variants ----
        else:
            method = verb_tag.lstrip("A").upper()
            if _is_session_self(args):
                url = args[1] if len(args) > 1 else kwargs.get("url", "")
            else:
                url = args[0] if len(args) > 0 else kwargs.get("url", "")

        return method, url

    def _prepare(url: str, method: str, headers: Optional[dict]):
        trace_id, allow = get_trace_and_should_propagate(url, skip)
        hdrs = dict(headers or {})
        if allow:
            hdrs[SAILFISH_TRACING_HEADER] = trace_id
        return trace_id, hdrs, int(time.time() * 1_000)

    def _record(trace_id, url, method, status, success, err, start_ms):
        record_network_request(
            trace_id,
            url,
            method,
            status or 0,
            success,
            err,
            timestamp_start=start_ms,
            timestamp_end=int(time.time() * 1_000),
        )

    # ----------------------------------------------------------------- header merge
    def _headers_pos_index(args: Tuple) -> Optional[int]:
        """
        Return the positional index that already holds a headers dict, or None.
        """
        if not args:
            return None
        if isinstance(args[0], (SessionCls, AsyncSessionCls)):
            return 3 if len(args) > 3 else None
        return 2 if len(args) > 2 else None

    def _inject_header(args: Tuple, kwargs: dict, key: str, val: str) -> Tuple:
        idx = _headers_pos_index(args)
        if idx is not None:
            merged = dict(args[idx] or {})
            merged[key] = val
            args = (*args[:idx], merged, *args[idx + 1 :])
        else:
            hdrs = dict(kwargs.get("headers") or {})
            hdrs[key] = val
            kwargs["headers"] = hdrs
        return args, kwargs

    # -------------------------------------------------------------------- wrappers
    def _wrap_sync(fn, verb_tag: str):
        def wrapper(*args, **kwargs):
            method, url = _resolve_method_url(verb_tag, args, kwargs)
            trace_id, _hdrs, t0 = _prepare(url, method, kwargs.get("headers"))
            args, kwargs = _inject_header(
                args, kwargs, SAILFISH_TRACING_HEADER, trace_id
            )

            status = 0
            success = False
            err = None
            try:
                resp = fn(*args, **kwargs)
                status = getattr(resp, "status_code", 0)
                success = True
                return resp
            except Exception as exc:  # noqa: BLE001
                err = str(exc)[:255]
                raise
            finally:
                _record(trace_id, url, method, status, success, err, t0)

        return wrapper

    def _wrap_async(fn, verb_tag: str):
        async def wrapper(*args, **kwargs):
            method, url = _resolve_method_url(verb_tag, args, kwargs)
            trace_id, _hdrs, t0 = _prepare(url, method, kwargs.get("headers"))
            args, kwargs = _inject_header(
                args, kwargs, SAILFISH_TRACING_HEADER, trace_id
            )

            status = 0
            success = False
            err = None
            try:
                resp = await fn(*args, **kwargs)
                status = getattr(resp, "status_code", 0)
                success = True
                return resp
            except Exception as exc:  # noqa: BLE001
                err = str(exc)[:255]
                raise
            finally:
                _record(trace_id, url, method, status, success, err, t0)

        return wrapper

    # ------------------------------------------------------------- apply patches
    niquests.request = _wrap_sync(niquests.request, "REQUEST")
    for v in verbs:
        setattr(niquests, v, _wrap_sync(getattr(niquests, v), v.upper()))

    SessionCls.request = _wrap_sync(SessionCls.request, "REQUEST")
    for v in verbs:
        setattr(SessionCls, v, _wrap_sync(getattr(SessionCls, v), v.upper()))

    if hasattr(niquests, "arequest"):
        niquests.arequest = _wrap_async(niquests.arequest, "AREQUEST")
        for av in verbs:
            async_name = f"a{av}"
            setattr(
                niquests,
                async_name,
                _wrap_async(getattr(niquests, async_name), async_name.upper()),
            )

    if hasattr(SessionCls, "arequest"):
        SessionCls.arequest = _wrap_async(SessionCls.arequest, "AREQUEST")
        for av in verbs:
            async_name = f"a{av}"
            setattr(
                SessionCls,
                async_name,
                _wrap_async(getattr(SessionCls, async_name), async_name.upper()),
            )

    if AsyncSessionCls is not type("._Dummy", (), {}):
        AsyncSessionCls.request = _wrap_async(AsyncSessionCls.request, "REQUEST")
        for v in verbs:
            setattr(
                AsyncSessionCls, v, _wrap_async(getattr(AsyncSessionCls, v), v.upper())
            )
