from typing import List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from .utils import get_trace_and_should_propagate, record_network_request


def patch_httpx(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    """
    Monkey-patch HTTPX to inject SAILFISH_TRACING_HEADER into
    all outbound requests (sync + async + streams), skipping any
    domains in domains_to_not_propagate_headers_to, and recording each.
    Safe to call even if HTTPX is not installed.
    """
    try:
        import httpx
    except ImportError:
        return  # No HTTPX installed—nothing to patch

    domains = domains_to_not_propagate_headers_to or []

    # Preserve originals
    orig_request = httpx.request
    orig_client_request = httpx.Client.request
    orig_async_request = httpx.AsyncClient.request
    orig_stream = httpx.stream
    orig_client_stream = httpx.Client.stream
    orig_async_client_stream = httpx.AsyncClient.stream

    # Shared header + record prep
    def _prepare(method: str, url: str, headers: Optional[dict]):
        trace_id, allow = get_trace_and_should_propagate(url, domains)
        hdrs = dict(headers or {})
        if allow:
            hdrs[SAILFISH_TRACING_HEADER] = trace_id
        return trace_id, hdrs

    # 1) Module-level request
    def _patched_request(method, url, *args, headers=None, **kwargs):
        trace_id, hdrs = _prepare(method, str(url), headers)
        resp = orig_request(method, url, *args, headers=hdrs, **kwargs)
        record_network_request(trace_id, str(url), method, resp.status_code, resp.is_success)
        return resp

    # 2) Sync Client.request
    def _patched_client_request(self, method, url, *args, headers=None, **kwargs):
        trace_id, hdrs = _prepare(method, str(url), headers)
        resp = orig_client_request(self, method, url, *args, headers=hdrs, **kwargs)
        record_network_request(trace_id, str(url), method, resp.status_code, resp.is_success)
        return resp

    # 3) AsyncClient.request
    async def _patched_async_request(self, method, url, *args, headers=None, **kwargs):
        trace_id, hdrs = _prepare(method, str(url), headers)
        resp = await orig_async_request(
            self, method, url, *args, headers=hdrs, **kwargs
        )
        record_network_request(trace_id, str(url), method, resp.status_code, resp.is_success)
        return resp

    # 4a) Module-level streaming
    def _patched_stream(method, url, *args, headers=None, **kwargs):
        trace_id, hdrs = _prepare(method, str(url), headers)
        cm = orig_stream(method, url, *args, headers=hdrs, **kwargs)

        class StreamCM:
            def __enter__(self):
                resp = cm.__enter__()
                resp.read()  # ensure .content
                record_network_request(
                    trace_id, url, method, resp.status_code, resp.is_success
                )
                return resp

            def __exit__(self, exc_type, exc, tb):
                return cm.__exit__(exc_type, exc, tb)

        return StreamCM()

    # 4b) Sync Client.stream()
    def _patched_client_stream(self, method, url, *args, headers=None, **kwargs):
        trace_id, hdrs = _prepare(method, str(url), headers)
        cm = orig_client_stream(self, method, url, *args, headers=hdrs, **kwargs)

        class ClientStreamCM:
            def __enter__(self):
                resp = cm.__enter__()
                resp.read()
                record_network_request(
                    trace_id, str(url), method, resp.status_code, resp.is_success
                )
                return resp

            def __exit__(self, exc_type, exc, tb):
                return cm.__exit__(exc_type, exc, tb)

        return ClientStreamCM()

    # 4c) AsyncClient.stream()
    def _patched_async_client_stream(self, method, url, *args, headers=None, **kwargs):
        trace_id, hdrs = _prepare(method, str(url), headers)
        cm = orig_async_client_stream(self, method, url, *args, headers=hdrs, **kwargs)

        class AsyncClientStreamCM:
            async def __aenter__(self):
                resp = await cm.__aenter__()
                await resp.aread()  # ensure .content
                record_network_request(
                    trace_id, str(url), method, resp.status_code, resp.is_success
                )
                return resp

            async def __aexit__(self, exc_type, exc, tb):
                return await cm.__aexit__(exc_type, exc, tb)

        return AsyncClientStreamCM()

    # Apply monkey-patches
    httpx.request = _patched_request
    httpx.Client.request = _patched_client_request
    httpx.AsyncClient.request = _patched_async_request
    httpx.stream = _patched_stream
    httpx.Client.stream = _patched_client_stream
    httpx.AsyncClient.stream = _patched_async_client_stream
