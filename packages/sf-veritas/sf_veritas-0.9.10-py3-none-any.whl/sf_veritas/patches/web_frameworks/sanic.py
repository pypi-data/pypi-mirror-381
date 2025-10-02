import inspect
import sysconfig
from functools import lru_cache

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code, _unwrap_user_func


def patch_sanic():
    """
    If Sanic is installed, monkey-patch Sanic.__init__ so every app:
      1) request middleware: pulls SAILFISH_TRACING_HEADER → ContextVar
      2) response middleware: emits exactly one NetworkHop from the
         first user-land frame of the handler that just ran.
    Safe no-op if Sanic isn't present.
    """
    print("[[patch_sanic]] patching sanic...", log=False)
    try:
        from sanic import Sanic
    except ImportError:
        return
    print("[[patch_sanic]] patching sanic...about to start", log=False)

    # ----------------------------------------------------------------- #
    # Patch __init__: install two middleware
    # ----------------------------------------------------------------- #
    orig_init = Sanic.__init__

    def patched_init(self, *args, **kwargs):
        """
        After the original Sanic app is created we attach:
        • request-middleware – capture `SAILFISH_TRACING_HEADER`
        • response-middleware – emit one NetworkHop
        • *NEW* universal exception handler – funnels every Exception
          (including Sanic HTTP errors) through `custom_excepthook`
          and then delegates to Sanic's default error handling chain.
        """
        # ---------------------------------------------------------------- #
        # Let Sanic build the app normally
        # ---------------------------------------------------------------- #
        orig_init(self, *args, **kwargs)

        # ─────────────────── 1) Inbound header capture ─────────────────── #
        async def _push_trace_id(request):
            hdr = request.headers.get(SAILFISH_TRACING_HEADER)
            if hdr:
                get_or_set_sf_trace_id(hdr, is_associated_with_inbound_request=True)

        try:
            self.register_middleware(_push_trace_id, attach_to="request")
        except TypeError:  # Sanic<22 compatibility
            self.register_middleware(_push_trace_id, "request")

        # ─────────────────── 2) NetworkHop emission ────────────────────── #
        async def _emit_hop(request, response):
            handler = getattr(request, "route", None)
            if not handler:
                return
            fn = getattr(handler, "handler", None)
            if not fn:
                return

            real_fn = _unwrap_user_func(fn)
            code = getattr(real_fn, "__code__", None)
            path = getattr(code, "co_filename", None)
            if not _is_user_code(path):
                return

            line_no = code.co_firstlineno
            name = real_fn.__name__
            _, session_id = get_or_set_sf_trace_id()  # already seeded

            if SF_DEBUG:
                print(
                    f"[[Sanic-hop]] {name} ({path}:{line_no}) session={session_id}",
                    log=False,
                )

            NetworkHopsTransmitter().send(
                session_id=session_id,
                line=str(line_no),
                column="0",
                name=name,
                entrypoint=path,
            )

        try:
            self.register_middleware(_emit_hop, attach_to="response")
        except TypeError:
            self.register_middleware(_emit_hop, "response")

        # ─────────────────── 3) Universal exception hook  NEW ──────────── #
        async def _capture_exception(request, exception):
            """
            Called for *any* exception – user errors, `abort|HTTPException`,
            or Sanic-specific errors. We forward to `custom_excepthook`
            and then fall back to Sanic's default error handler so
            behaviour is unchanged.
            """
            custom_excepthook(type(exception), exception, exception.__traceback__)
            # Delegate to default handler to keep standard 4xx/5xx payload
            response = request.app.error_handler.default(request, exception)
            if inspect.isawaitable(response):
                response = await response
            return response

        # Register for the base `Exception` class to catch everything
        self.error_handler.add(Exception, _capture_exception)

        if SF_DEBUG:
            print(
                "[[patch_sanic]] tracing middlewares + exception handler added",
                log=False,
            )

    Sanic.__init__ = patched_init
