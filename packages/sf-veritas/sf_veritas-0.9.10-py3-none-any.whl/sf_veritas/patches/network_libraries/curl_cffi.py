import time
from typing import List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from ..constants import supported_network_verbs as verbs
from .utils import get_trace_and_should_propagate, record_network_request


def patch_curl_cffi(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    """
    Monkey-patch curl_cffi.requests so that EVERY HTTP verb
    injects SAILFISH_TRACING_HEADER (when allowed) and then records the request.
    """
    try:
        import curl_cffi.requests as ccr
    except ImportError:
        return

    skip = domains_to_not_propagate_headers_to or []

    def make_wrapper(orig_fn, verb_name):
        def wrapper(*args, **kwargs):
            # 1) Determine HTTP method and URL safely
            if verb_name == "request":
                # support both request(url) and request(method, url, …)
                if len(args) == 1 and isinstance(args[0], str):
                    method, url = "GET", args[0]
                elif len(args) >= 2 and isinstance(args[0], str):
                    method, url = args[0].upper(), args[1]
                elif len(args) >= 3:
                    # bound Session.request(self, method, url, …)
                    method, url = args[1].upper(), args[2]
                else:
                    method = kwargs.get("method", "").upper()
                    url = kwargs.get("url", "")
            else:
                method = verb_name.upper()
                # for module-level: args[0] == url
                # for bound: args[1] == url
                if len(args) >= 1 and isinstance(args[0], str):
                    url = args[0]
                elif len(args) >= 2:
                    url = args[1]
                else:
                    url = kwargs.get("url", "")

            # 2) Trace-id + skip-list check
            trace_id, allow = get_trace_and_should_propagate(url, skip)
            headers = kwargs.get("headers", {}) or {}
            if allow:
                headers[SAILFISH_TRACING_HEADER] = trace_id
            kwargs["headers"] = headers

            # 3) Perform the real call
            start = int(time.time() * 1_000)
            resp = orig_fn(*args, **kwargs)
            end = int(time.time() * 1_000)

            # 4) Record the network request
            status = getattr(resp, "status_code", None) or getattr(resp, "status", 0)
            ok = getattr(resp, "ok", status < 400)
            error = None if ok else getattr(resp, "text", str(resp))[:255]

            record_network_request(
                trace_id,
                url,
                method,
                status,
                ok,
                error,
                timestamp_start=start,
                timestamp_end=end,
            )

            return resp

        return wrapper

    # Patch module-level verbs
    for verb in verbs:
        orig = getattr(ccr, verb, None)
        if orig:
            setattr(ccr, verb, make_wrapper(orig, verb))

    # Patch Session & AsyncSession methods
    for cls_name in ("Session", "AsyncSession"):
        cls = getattr(ccr, cls_name, None)
        if not cls:
            continue
        for verb in verbs:
            orig = getattr(cls, verb, None)
            if orig:
                setattr(cls, verb, make_wrapper(orig, verb))
