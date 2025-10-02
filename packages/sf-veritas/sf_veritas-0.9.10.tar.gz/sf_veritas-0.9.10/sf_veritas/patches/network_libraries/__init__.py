from typing import List, Optional

from .aiohttp import patch_aiohttp
from .curl_cffi import patch_curl_cffi
from .http_client import patch_http_client
from .httpcore import patch_httpcore
from .httplib2 import patch_httplib2
from .httpx import patch_httpx
from .niquests import patch_niquests
from .pycurl import patch_pycurl
from .requests import patch_requests
from .tornado import patch_tornado
from .treq import patch_treq
from .urllib_request import patch_urllib_request

# from .aioh2            import patch_aioh2           # Asynchronous HTTP/2 client, no clear extension hooks
# from .http_prompt      import patch_http_prompt     # CLI HTTP client, minimal public API
# from .mureq            import patch_mureq           # Specialized crawler client, little documentation
# from .reqboost         import patch_reqboost        # High-performance batch client, docs scarce
# from .impit            import (patch_impit)         # Used by Crawlee's ImpitHttpClient
# from .h11              import patch_h11             # Low-level HTTP/1.1 protocol library
# from .aioquic          import patch_aioquic         # QUIC/HTTP-3 client, no standard headers API
# from .qh3              import patch_qh3             # Experimental HTTP/3 client, no docs found


def patch_all_http_clients(
    domains_to_not_propagate_headers_to: Optional[List[str]] = None,
):
    # fully implemented patches
    patch_requests(domains_to_not_propagate_headers_to)
    patch_urllib_request(domains_to_not_propagate_headers_to)
    patch_http_client(domains_to_not_propagate_headers_to)
    patch_httplib2(domains_to_not_propagate_headers_to)
    patch_pycurl(domains_to_not_propagate_headers_to)
    patch_treq(domains_to_not_propagate_headers_to)
    patch_httpx(domains_to_not_propagate_headers_to)
    patch_aiohttp(domains_to_not_propagate_headers_to)
    patch_tornado(domains_to_not_propagate_headers_to)
    patch_curl_cffi(domains_to_not_propagate_headers_to)
    patch_httpcore(domains_to_not_propagate_headers_to)
    patch_niquests(domains_to_not_propagate_headers_to)

    # # Lesser-used libraries
    # patch_impit(domains_to_not_propagate_headers_to)
    # patch_aioh2(domains_to_not_propagate_headers_to)
    # patch_http_prompt(domains_to_not_propagate_headers_to)
    # patch_mureq(domains_to_not_propagate_headers_to)
    # patch_reqboost(domains_to_not_propagate_headers_to)
    # patch_h11(domains_to_not_propagate_headers_to)
    # patch_aioquic(domains_to_not_propagate_headers_to)
    # patch_qh3(domains_to_not_propagate_headers_to)
