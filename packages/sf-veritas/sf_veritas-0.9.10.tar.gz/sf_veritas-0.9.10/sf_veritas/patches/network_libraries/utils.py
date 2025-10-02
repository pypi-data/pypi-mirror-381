"""
Shared helpers used by all network-patch modules.
"""

from __future__ import annotations

import time
from typing import List, Tuple
from urllib.parse import urlparse

from ...regular_data_transmitter import NetworkRequestTransmitter
from ...thread_local import get_or_set_sf_trace_id, is_network_recording_suppressed


###############################################################################
# Domain-parsing utility  (no external network / no tldextract needed)
###############################################################################
def extract_domain(url: str) -> str:
    """
    Return a canonical host name for header-propagation checks.

    • Works entirely offline (std-lib only) – no remote download or file locks.
    • Keeps sub-domains intact, just strips a leading “www.” and port numbers.

    Examples
    --------
    >>> extract_domain("https://www.example.com:443/path")
    'example.com'
    >>> extract_domain("https://api.foo.bar.example.co.uk/v1")
    'api.foo.bar.example.co.uk'
    """
    try:
        host = urlparse(url).hostname or url
    except Exception:
        host = url  # fall back to raw string on malformed URLs
    if host.startswith("www."):
        host = host[4:]
    return host.lower()


###############################################################################
# Header-propagation + network-recording helpers
###############################################################################
def get_trace_and_should_propagate(
    url: str,
    domains_to_not_propagate: List[str],
) -> Tuple[str, bool]:
    """
    Returns  (trace_id, should_propagate?)  for the given destination `url`.
    """
    _, trace_id = get_or_set_sf_trace_id()
    domain = extract_domain(url)
    allow_header = domain not in domains_to_not_propagate
    return trace_id, allow_header


def record_network_request(
    trace_id: str,
    url: str,
    method: str,
    status_code: int,
    success: bool,
    error: str | None = None,
    timestamp_start: int | None = None,
    timestamp_end: int | None = None,
) -> None:
    """
    Fire off a GraphQL NetworkRequest mutation via NetworkRequestTransmitter.
    Handles tripartite trace-ID splitting and default timestamps.
    """
    if is_network_recording_suppressed():
        return

    session_id, page_visit_id, request_id = None, None, None
    parts = trace_id.split("/")
    if parts:
        session_id = parts[0]
    if len(parts) > 1:
        page_visit_id = parts[1]
    if len(parts) > 2:
        request_id = parts[2]

    now_ms = lambda: int(time.time() * 1_000)  # noqa: E731
    ts0 = timestamp_start or now_ms()
    ts1 = timestamp_end or now_ms()

    NetworkRequestTransmitter().do_send(
        (
            request_id,
            page_visit_id,
            session_id,
            None,  # service_uuid (set by transmitter middleware)
            ts0,
            ts1,
            status_code,
            success,
            None if success else (error or "")[:255],
            url,
            method.upper(),
        )
    )
