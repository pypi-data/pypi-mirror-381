import time
from typing import List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from .utils import get_trace_and_should_propagate, record_network_request


def patch_http_client(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    # ensure we always have a list
    if domains_to_not_propagate_headers_to is None:
        domains_to_not_propagate_headers_to = []

    try:
        import http.client as _hc
    except ImportError:
        return

    original_request = _hc.HTTPConnection.request

    def patched_request(
        self, method, url, body=None, headers=None, *, encode_chunked=False
    ):
        # timestamp for recording
        start_ts = int(time.time() * 1_000)

        # get the trace_id and check if we should propagate
        trace_id, allow = get_trace_and_should_propagate(
            url, domains_to_not_propagate_headers_to
        )

        # copy headers and inject only if allowed
        headers = headers.copy() if headers else {}
        if allow:
            headers[SAILFISH_TRACING_HEADER] = trace_id

        try:
            # perform the real request
            result = original_request(
                self,
                method,
                url,
                body=body,
                headers=headers,
                encode_chunked=encode_chunked,
            )
            # fire off our network-record GraphQL mutation
            record_network_request(
                trace_id, url, method, 0, True, timestamp_start=start_ts
            )
            return result
        except Exception as e:
            # record failures too
            record_network_request(
                trace_id,
                url,
                method,
                0,
                False,
                error=str(e),
                timestamp_start=start_ts,
            )
            raise

    _hc.HTTPConnection.request = patched_request
