"""
• SFTracingASGIMiddleware: propagates SAILFISH_TRACING_HEADER inbound → ContextVar.
• SFTracingRoute:   per-endpoint hop capture (user code only).
• patch_fastapi():  monkey-patch FastAPI.__init__ to inject both.
"""

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code, _unwrap_user_func

# ---------- FastAPI / Starlette imports (guarded) ----------
try:
    import fastapi
    from fastapi.requests import Request
    from fastapi.routing import APIRoute
    from starlette.types import ASGIApp, Receive, Scope, Send
except ImportError:  # FastAPI not installed – expose no-op

    def patch_fastapi():
        return

else:

    # ========================================================
    # 1. Context-propagation middleware (already present)
    # ========================================================
    class SFTracingASGIMiddleware:
        """Fastest possible ASGI middleware (no BaseHTTPMiddleware).

        • Captures inbound SAILFISH_TRACING_HEADER header → ContextVar
        • Catches all unhandled exceptions and funnels them through
        `custom_excepthook`.
        """

        def __init__(self, app: ASGIApp):
            self.app = app

        async def __call__(self, scope: Scope, receive: Receive, send: Send):
            # 1) Header capture (HTTP requests only)
            if scope.get("type") == "http":
                hdr = next(
                    (
                        val.decode()
                        for name, val in scope.get("headers", [])
                        if name.decode().lower() == SAILFISH_TRACING_HEADER.lower()
                    ),
                    None,
                )
                if hdr:
                    get_or_set_sf_trace_id(hdr, is_associated_with_inbound_request=True)

            # 2) Execute downstream app and trap unhandled exceptions
            try:
                await self.app(scope, receive, send)
            except Exception as exc:  # noqa: BLE001
                custom_excepthook(type(exc), exc, exc.__traceback__)
                raise  # re-raise so FastAPI still returns a 500 response

    # ========================================================
    # 2. Hop-capturing APIRoute
    # ========================================================
    class SFTracingRoute(APIRoute):
        """
        Custom APIRoute that

        • fires a single NetworkHop when user-code starts (skips Strawberry), and
        • funnels **any** exception – including FastAPI's HTTPException – through
        `custom_excepthook` before letting FastAPI continue its normal handling.
        """

        async def _emit_hop_if_needed(self, request: Request):
            _, session_id = get_or_set_sf_trace_id()  # already seeded by middleware

            endpoint_fn = _unwrap_user_func(self.endpoint)
            filename = getattr(endpoint_fn, "__code__", None).co_filename

            # Ignore non-user / Strawberry endpoints
            if (
                not filename
                or not _is_user_code(filename)
                or endpoint_fn.__module__.startswith("strawberry")
            ):
                return

            line_no = endpoint_fn.__code__.co_firstlineno
            name = endpoint_fn.__name__

            if SF_DEBUG:
                print(
                    f"[[SFTracingRoute]] hop → {name} ({filename}:{line_no}) "
                    f"session={session_id}",
                    log=False,
                )

            NetworkHopsTransmitter().send(
                session_id=session_id,
                line=str(line_no),
                column="0",
                name=name,
                entrypoint=filename,
            )

        # ------------------------------------------------------------------ #
        # override FastAPI's handler factory so we can trap *all* exceptions
        # ------------------------------------------------------------------ #
        def get_route_handler(self):
            original_route_handler = super().get_route_handler()

            async def traced_route_handler(request: Request):
                try:
                    await self._emit_hop_if_needed(request)
                    return await original_route_handler(request)
                except Exception as exc:  # <-- catches
                    custom_excepthook(type(exc), exc, exc.__traceback__)  # all FastAPI
                    raise  # exceptions

            return traced_route_handler

    # ========================================================
    # 3. Monkey-patch FastAPI.__init__
    # ========================================================
    def patch_fastapi():
        """
        • Inject SFTracingASGIMiddleware at app start-up.
        • Force router.route_class = SFTracingRoute to wrap every endpoint.
        """
        original_init = fastapi.FastAPI.__init__

        def patched_init(self, *args, **kwargs):
            # Let FastAPI do its normal work first.
            original_init(self, *args, **kwargs)
            # Insert ASGI middleware at the very top.
            self.add_middleware(SFTracingASGIMiddleware)
            # Ensure all new routes use our tracing route class.
            self.router.route_class = SFTracingRoute
            if SF_DEBUG:
                print(
                    "[[patch_fastapi]] Tracing middleware + route class installed",
                    log=False,
                )

        fastapi.FastAPI.__init__ = patched_init
