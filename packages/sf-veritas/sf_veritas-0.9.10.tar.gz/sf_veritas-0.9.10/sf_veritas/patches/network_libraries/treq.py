"""
Header propagation + network-recording patch for **Treq**.

• Propagates SAILFISH_TRACING_HEADER (unless excluded destination).
• Records every outbound request via record_network_request(…).

It also guarantees that Twisted's reactor is *running*:

1. Prefer installing the asyncio reactor early.
2. If a different reactor is already installed, start it in a background thread
   (if it isn't running yet), so Deferreds produced by treq will fire.
"""

from __future__ import annotations

import asyncio
import threading
import time
from typing import List, Optional

from ...constants import SAILFISH_TRACING_HEADER
from ..constants import supported_network_verbs as verbs
from .utils import get_trace_and_should_propagate, record_network_request


def _ensure_reactor_running() -> None:
    """
    • Try to replace Twisted's default reactor with the asyncio one.
    • If that fails because a reactor is already installed, make sure the
      existing reactor is *running* (start it in a daemon thread if needed).
    """
    # Twisted import must be inside this function to avoid premature reactor load
    from twisted.internet import reactor

    try:
        from twisted.internet import asyncioreactor

        # Already an asyncio reactor? -> nothing to do
        if reactor.__class__.__module__ == "twisted.internet.asyncioreactor":
            return

        # Try upgrade to asyncio-reactor (will raise if another reactor in use)
        asyncioreactor.install(asyncio.get_event_loop())  # type: ignore[arg-type]
        return
    except Exception:
        # Could not swap reactors (already installed).  Make sure current one runs.
        if not reactor.running:
            threading.Thread(
                target=reactor.run,
                kwargs={"installSignalHandlers": False},
                daemon=True,
            ).start()


def patch_treq(domains_to_not_propagate_headers_to: Optional[List[str]] = None):
    try:
        # Ensure a live reactor *before* importing treq
        _ensure_reactor_running()

        import treq
    except ImportError:
        return  # treq is not installed; nothing to patch

    exclude = domains_to_not_propagate_headers_to or []
    orig_request = treq.request

    # ------------------------------------------------------------------ #
    def patched_request(method: str, url: str, **kwargs):
        # -------- header propagation
        hdrs = dict(kwargs.pop("headers", {}) or {})
        trace_id, allow = get_trace_and_should_propagate(url, exclude)
        if allow:
            hdrs[SAILFISH_TRACING_HEADER] = trace_id
        kwargs["headers"] = hdrs

        t0 = int(time.time() * 1_000)
        d = orig_request(method, url, **kwargs)  # Deferred

        # -------- record on success
        def _ok(resp):
            status = getattr(resp, "code", 0)
            record_network_request(
                trace_id,
                url,
                method.upper(),
                status,
                status < 400,
                None,
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )
            return resp

        # -------- record on failure
        def _err(f):
            record_network_request(
                trace_id,
                url,
                method.upper(),
                0,
                False,
                str(f.value)[:255],
                timestamp_start=t0,
                timestamp_end=int(time.time() * 1_000),
            )
            return f

        d.addCallbacks(_ok, _err)
        return d

    treq.request = patched_request  # type: ignore[assignment]

    # Convenience verbs → reuse patched_request
    def _verb_factory(v: str):
        def _verb(url, **k):
            return treq.request(v.upper(), url, **k)

        _verb.__name__ = v
        return _verb

    for verb in verbs:
        setattr(treq, verb, _verb_factory(verb))
