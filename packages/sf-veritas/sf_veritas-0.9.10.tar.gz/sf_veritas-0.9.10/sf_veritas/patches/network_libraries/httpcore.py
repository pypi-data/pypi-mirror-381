import time
from typing import List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from .utils import get_trace_and_should_propagate, record_network_request


def patch_httpcore(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    """
    Monkey-patch httpcore.ConnectionPool and AsyncConnectionPool
    to inject SAILFISH_TRACING_HEADER (unless excluded)
    and to record every outbound request.
    """
    try:
        import httpcore
    except ImportError:
        return  # HTTP Core not present—skip patch

    # Keep original methods
    orig_sync_req = httpcore.ConnectionPool.request
    orig_sync_stream = httpcore.ConnectionPool.stream
    orig_async_req = httpcore.AsyncConnectionPool.request
    orig_async_stream = httpcore.AsyncConnectionPool.stream

    # Normalize exclude list
    exclude = domains_to_not_propagate_headers_to or []

    def _prepare_headers(url, existing_headers):
        """
        Returns (new_headers, trace_id).
        Only injects if domain not in `exclude`.
        """
        trace_id, allow = get_trace_and_should_propagate(url, exclude)
        if not allow:
            return list(existing_headers or []), trace_id
        hdrs = list(existing_headers or [])
        hdrs.append((SAILFISH_TRACING_HEADER.encode(), trace_id.encode()))
        return hdrs, trace_id

    # 1. Sync .request(...)
    def _patched_sync_request(self, method, url, **kwargs):
        ts0 = int(time.time() * 1_000)
        # prepare headers & trace
        headers, trace_id = _prepare_headers(url, kwargs.get("headers"))
        kwargs["headers"] = headers

        error = None
        try:
            resp = orig_sync_req(self, method, url, **kwargs)
            success = True
            status = getattr(resp, "status_code", 0)
            return resp
        except Exception as e:
            success = False
            status = 0
            error = str(e)[:255]
            raise
        finally:
            ts1 = int(time.time() * 1_000)
            record_network_request(
                trace_id, url, method, status, success, error, ts0, ts1
            )

    # 2. Sync .stream(...)
    def _patched_sync_stream(self, method, url, **kwargs):
        ts0 = int(time.time() * 1_000)
        headers, trace_id = _prepare_headers(url, kwargs.get("headers"))
        kwargs["headers"] = headers

        error = None
        try:
            stream = orig_sync_stream(self, method, url, **kwargs)
            success = True
            # stream itself yields the body; status often on returned object
            status = 0
            return stream
        except Exception as e:
            success = False
            status = 0
            error = str(e)[:255]
            raise
        finally:
            ts1 = int(time.time() * 1_000)
            record_network_request(
                trace_id, url, method, status, success, error, ts0, ts1
            )

    # 3. Async .request(...)
    async def _patched_async_request(self, method, url, **kwargs):
        ts0 = int(time.time() * 1_000)
        headers, trace_id = _prepare_headers(url, kwargs.get("headers"))
        kwargs["headers"] = headers

        error = None
        try:
            resp = await orig_async_req(self, method, url, **kwargs)
            success = True
            status = getattr(resp, "status_code", 0)
            return resp
        except Exception as e:
            success = False
            status = 0
            error = str(e)[:255]
            raise
        finally:
            ts1 = int(time.time() * 1_000)
            record_network_request(
                trace_id, url, method, status, success, error, ts0, ts1
            )

    # 4. Async .stream(...)
    def _patched_async_stream(self, method, url, **kwargs):
        ts0 = int(time.time() * 1_000)
        headers, trace_id = _prepare_headers(url, kwargs.get("headers"))
        kwargs["headers"] = headers
        original_cm = orig_async_stream(self, method, url, **kwargs)

        class _StreamCM:
            def __init__(self, cm):
                self._cm = cm
                self._status = 0

            async def __aenter__(self):
                response = await self._cm.__aenter__()  # now a single Response
                # capture status (httpcore.Response.status or status_code)
                self._status = getattr(
                    response, "status_code", getattr(response, "status", 0)
                )
                return response

            async def __aexit__(self, exc_type, exc, tb):
                success = exc_type is None
                ts1 = int(time.time() * 1_000)
                record_network_request(
                    trace_id,
                    url,
                    method,
                    self._status,
                    success,
                    None if success else str(exc)[:255],
                    ts0,
                    ts1,
                )
                return await self._cm.__aexit__(exc_type, exc, tb)

        return _StreamCM(original_cm)

    # Apply patches
    httpcore.ConnectionPool.request = _patched_sync_request
    httpcore.ConnectionPool.stream = _patched_sync_stream
    httpcore.AsyncConnectionPool.request = _patched_async_request
    httpcore.AsyncConnectionPool.stream = _patched_async_stream
