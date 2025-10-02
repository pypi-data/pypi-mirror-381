import time
from typing import List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from .utils import get_trace_and_should_propagate, record_network_request


def patch_httplib2(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    """
    Monkey-patch httplib2.Http.request so that:
    1. We skip header injection for configured domains.
    2. We call NetworkRequestTransmitter().do_send via record_network_request().
    3. All HTTP methods (GET, POST, etc.) continue to work as before.
    """
    try:
        import httplib2
    except ImportError:
        return

    # default to an empty blocklist
    if domains_to_not_propagate_headers_to is None:
        domains_to_not_propagate_headers_to = []

    original_request = httplib2.Http.request

    def patched_request(self, uri, method="GET", body=None, headers=None, **kwargs):
        start_ts = int(time.time() * 1_000)
        # decide whether to inject header
        trace_id, allow = get_trace_and_should_propagate(
            uri, domains_to_not_propagate_headers_to
        )
        # prepare headers
        headers = headers.copy() if headers else {}
        if allow:
            headers[SAILFISH_TRACING_HEADER] = trace_id

        try:
            # perform the actual HTTP call
            response, content = original_request(
                self, uri, method, body=body, headers=headers, **kwargs
            )
            status_code = getattr(response, "status", None) or getattr(
                response, "status_code", None
            )
            success = isinstance(status_code, int) and 200 <= status_code < 400
            return response, content

        except Exception as e:
            # record failures
            record_network_request(
                trace_id,
                uri,
                method,
                0,
                False,
                error=str(e)[:255],
                timestamp_start=start_ts,
                timestamp_end=int(time.time() * 1_000),
            )
            raise

        finally:
            # record successes
            if "status_code" in locals():
                record_network_request(
                    trace_id,
                    uri,
                    method,
                    status_code,
                    success,
                    timestamp_start=start_ts,
                    timestamp_end=int(time.time() * 1_000),
                )

    # apply our patch
    httplib2.Http.request = patched_request
