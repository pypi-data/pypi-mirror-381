import time
from typing import Any, List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from .utils import get_trace_and_should_propagate, record_network_request


def patch_aiohttp(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    """
    Monkey-patch aiohttp so that every HTTP verb:
        1) injects SAILFISH_TRACING_HEADER when allowed,
        2) measures timing,
        3) calls NetworkRequestTransmitter().do_send via record_network_request.
    """
    try:
        import aiohttp
    except:
        return

    skip = domains_to_not_propagate_headers_to or []

    # 1) Patch the core ClientSession._request coroutine
    orig_request = aiohttp.ClientSession._request

    async def patched_request(self, verb_name: str, url: Any, **kwargs):
        trace_id, allow = get_trace_and_should_propagate(str(url), skip)
        headers = kwargs.get("headers", {}) or {}
        if allow:
            headers[SAILFISH_TRACING_HEADER] = trace_id
        kwargs["headers"] = headers

        # 2) Perform & time the request
        start = int(time.time() * 1_000)
        response = await orig_request(self, verb_name, url, **kwargs)
        end = int(time.time() * 1_000)

        # 3) Record outcome
        status = getattr(response, "status", 0)
        ok = status < 400
        error = None
        if not ok:
            try:
                text = await response.text()
                error = text[:255]
            except Exception:
                pass

        record_network_request(
            trace_id,
            str(url),
            verb_name.upper(),
            status,
            ok,
            error,
            timestamp_start=start,
            timestamp_end=end,
        )
        return response

    aiohttp.ClientSession._request = patched_request

    # 2) Also patch the module-level aiohttp.request coroutine
    orig_module_request = getattr(aiohttp, "request", None)
    if orig_module_request:

        async def patched_module_request(verb_name: str, url: str, **kwargs):
            trace_id, allow = get_trace_and_should_propagate(str(url), skip)
            headers = kwargs.get("headers", {}) or {}
            if allow:
                headers[SAILFISH_TRACING_HEADER] = trace_id
            kwargs["headers"] = headers

            start = int(time.time() * 1_000)
            response = await orig_module_request(verb_name, url, **kwargs)
            end = int(time.time() * 1_000)

            status = getattr(response, "status", getattr(response, "status_code", 0))
            ok = status < 400
            error = None
            if not ok:
                try:
                    body = await response.text()
                    error = body[:255]
                except Exception:
                    pass

            record_network_request(
                trace_id,
                str(url),
                verb_name.upper(),
                status,
                ok,
                error,
                timestamp_start=start,
                timestamp_end=end,
            )

            return response

        aiohttp.request = patched_module_request
