import time
from typing import List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from .utils import get_trace_and_should_propagate, record_network_request


def patch_pycurl(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    try:
        import pycurl
    except ImportError:
        return

    _OrigCurl = pycurl.Curl

    class WrappedCurl(_OrigCurl):  # ➊ subclass libcurl handle
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._sf_url: str | None = None
            self._sf_method: str | None = None
            self._sf_headers: list[str] = []

        # --- intercept option setting -------------------------------------------------
        def setopt(self, opt, val):
            if opt == pycurl.URL:
                self._sf_url = val
            elif opt == pycurl.CUSTOMREQUEST:
                self._sf_method = val.upper()
            elif opt == pycurl.HTTPHEADER:
                self._sf_headers = list(val)
            return super().setopt(opt, val)

        # --- wrapped perform() --------------------------------------------------------
        def perform(self):
            url = self._sf_url or ""
            method = (self._sf_method or "GET").upper()

            trace_id, allow = get_trace_and_should_propagate(
                url, domains_to_not_propagate_headers_to or []
            )

            # Build merged header list
            merged = list(self._sf_headers)
            if allow:
                merged.append(f"{SAILFISH_TRACING_HEADER}: {trace_id}")

            # Let libcurl negotiate & decode encodings for us
            super().setopt(pycurl.ACCEPT_ENCODING, "")

            # push merged headers down
            # NOTE: HTTPHEADER expects List[str] (or List[bytes]), ensure consistency
            super().setopt(pycurl.HTTPHEADER, merged)

            # timing / status / error capture
            ts0 = int(time.time() * 1_000)
            status = 0
            err: str | None = None
            try:
                rv = super().perform()
                status = int(self.getinfo(pycurl.RESPONSE_CODE) or 0)
                return rv
            except Exception as e:
                err = str(e)[:255]
                raise
            finally:
                ts1 = int(time.time() * 1_000)
                record_network_request(
                    trace_id, url, method, status, err is None, err, ts0, ts1
                )

    pycurl.Curl = WrappedCurl
