"""
• NetworkHopMiddleware: pure ASGI middleware that
  - pulls SAILFISH_TRACING_HEADER → ContextVar
  - installs a one-shot sys.setprofile tracer to catch the first user frame
• patch_starlette(): idempotent—monkey-patches Starlette.__init__
  to insert NetworkHopMiddleware on every app, before any routes fire.
"""

import inspect
import sys
import sysconfig
from typing import Optional

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id

# Guard so we only patch once
_starlette_patched = False

try:
    from starlette.applications import Starlette
    from starlette.types import ASGIApp, Receive, Scope, Send
except ImportError:

    def patch_starlette():
        return

else:
    # Pre-compute stdlib path for user-code checks
    _STDLIB_PATH = sysconfig.get_paths()["stdlib"]

    def _is_user_code(path: Optional[str] = None) -> bool:
        """Return True if filename is in user code (not stdlib or site-packages)."""
        if not path or path.startswith("<"):
            return False
        if path.startswith(_STDLIB_PATH):
            return False
        if "site-packages" in path or "dist-packages" in path:
            return False
        return True

    def patch_starlette():
        global _starlette_patched
        if _starlette_patched:
            return
        _starlette_patched = True

        # ----------------- profiler tracer factory -----------------
        def _make_tracer(info_scope: Scope):
            def tracer(frame, event, arg):
                if event == "call" and _is_user_code(frame.f_code.co_filename):
                    # First user frame: emit NetworkHop
                    _, session_id = get_or_set_sf_trace_id()
                    NetworkHopsTransmitter().send(
                        session_id=session_id,
                        line=str(frame.f_lineno),
                        column="0",
                        name=frame.f_code.co_name,
                        entrypoint=frame.f_code.co_filename,
                    )
                    # Stop profiling this request
                    sys.setprofile(None)
                return tracer

            return tracer

        # ----------------- ASGI middleware -----------------
        class NetworkHopMiddleware:
            """
            ASGI middleware that

            1) Pulls the inbound SAILFISH_TRACING_HEADER → ContextVar.
            2) Installs a one-shot ``sys.setprofile`` tracer to record the first
            *user-land* frame in the request (sends a NetworkHop).
            3) Funnels **all** exceptions - including Starlette/HTTPException - through
            ``custom_excepthook`` before letting Starlette continue its normal
            error handling.
            """

            def __init__(self, app: ASGIApp):
                self.app = app

            async def __call__(self, scope: Scope, receive: Receive, send: Send):
                profiler_installed = False

                if scope.get("type") == "http":
                    # --- 1) header capture ---------------------------------------
                    headers = {
                        k.decode().lower(): v.decode()
                        for k, v in scope.get("headers", [])
                    }
                    hdr = headers.get(SAILFISH_TRACING_HEADER.lower())
                    if hdr:
                        get_or_set_sf_trace_id(
                            hdr, is_associated_with_inbound_request=True
                        )

                    # --- 2) install one-shot profiler ---------------------------
                    import sys

                    def _tracer(frame, event, arg):
                        if event == "call" and _is_user_code(frame.f_code.co_filename):
                            _, session_id = get_or_set_sf_trace_id()
                            NetworkHopsTransmitter().send(
                                session_id=session_id,
                                line=str(frame.f_lineno),
                                column="0",
                                name=frame.f_code.co_name,
                                entrypoint=frame.f_code.co_filename,
                            )
                            sys.setprofile(None)  # disable after first hop
                        return _tracer

                    sys.setprofile(_tracer)
                    profiler_installed = True

                # --- 3) run downstream app and trap *all* exceptions ------------
                try:
                    await self.app(scope, receive, send)
                except Exception as exc:  # ← catches HTTPException too
                    custom_excepthook(type(exc), exc, exc.__traceback__)
                    raise  # Let Starlette build the 4xx/5xx response
                finally:
                    if profiler_installed:
                        sys.setprofile(None)  # safety-net
                    sys.setprofile(None)

        # ----------------- patch Starlette init -----------------
        original_init = Starlette.__init__

        def patched_init(self, *args, **kwargs):
            # 1) Run the original constructor
            original_init(self, *args, **kwargs)

            # 2) Insert our ASGI middleware at the top
            self.add_middleware(NetworkHopMiddleware)

            if SF_DEBUG:
                print("[[patch_starlette]] Installed NetworkHopMiddleware", log=False)

        Starlette.__init__ = patched_init
