from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code, _unwrap_user_func  # cached helpers


# ------------------------------------------------------------------------------------
# 1. Hop-capturing plugin ----------------------------------------------------------------
# ------------------------------------------------------------------------------------
class _SFTracingPlugin:
    """Bottle plugin (API v2) – wraps each route callback exactly once."""

    name = "sf_network_hop"
    api = 2

    def apply(self, callback, route):
        # 1. Resolve real user function
        real_fn = _unwrap_user_func(callback)
        mod = real_fn.__module__
        code = getattr(real_fn, "__code__", None)

        # 2. Skip library frames and Strawberry GraphQL handlers
        if (
            not code
            or not _is_user_code(code.co_filename)
            or mod.startswith("strawberry")
        ):
            return callback  # no wrapping

        filename, line_no, fn_name = (
            code.co_filename,
            code.co_firstlineno,
            real_fn.__name__,
        )
        hop_key = (filename, line_no)

        # 3. Wrapper that emits exactly one hop per request
        from bottle import request  # local to avoid hard dep

        def _wrapped(*args, **kwargs):  # noqa: ANN001
            sent = request.environ.setdefault("_sf_hops_sent", set())
            if hop_key not in sent:
                _, session_id = get_or_set_sf_trace_id()

                if SF_DEBUG:
                    print(
                        f"[[SFTracingBottle]] hop → {fn_name} "
                        f"({filename}:{line_no}) session={session_id}",
                        log=False,
                    )

                NetworkHopsTransmitter().send(
                    session_id=session_id,
                    line=str(line_no),
                    column="0",
                    name=fn_name,
                    entrypoint=filename,
                )
                sent.add(hop_key)

            return callback(*args, **kwargs)

        return _wrapped


# ------------------------------------------------------------------------------------
# 2. Context-propagation hook ---------------------------------------------------------
# ------------------------------------------------------------------------------------
def _install_before_request(app):
    from bottle import request

    @app.hook("before_request")
    def _extract_sf_trace_id():
        if hdr := request.headers.get(SAILFISH_TRACING_HEADER):
            get_or_set_sf_trace_id(hdr, is_associated_with_inbound_request=True)


# ------------------------------------------------------------------------------------
# NEW: Global error-handler wrapper for Bottle
# ------------------------------------------------------------------------------------
def _install_error_handler(app):
    """
    Replace ``app.default_error_handler`` so *any* exception or HTTPError
    (including those raised via ``abort()`` or ``HTTPError(status=500)``)
    is reported to ``custom_excepthook`` before Bottle builds the response.

    Bottle always funnels errors through this function, regardless of debug
    mode. See Bottle docs on *Error Handlers*.
    """
    original_handler = app.default_error_handler

    def _sf_error_handler(error):
        # Forward full traceback (HTTPError keeps it on .__traceback__)
        custom_excepthook(type(error), error, getattr(error, "__traceback__", None))
        return original_handler(error)

    app.default_error_handler = _sf_error_handler


# ------------------------------------------------------------------------------------
# 3. Public patch function – call this once at startup
# ------------------------------------------------------------------------------------
def patch_bottle():
    """
    • Adds before_request header propagation.
    • Installs NetworkHop plugin (covers all current & future routes).
    • Wraps default_error_handler so exceptions (incl. HTTPError 500) are captured.
    Safe no-op if Bottle is not installed or already patched.
    """
    try:
        import bottle
    except ImportError:  # Bottle absent
        return

    if getattr(bottle.Bottle, "__sf_tracing_patched__", False):
        return

    # ---- patch Bottle.__init__ ----------------------------------------------------
    original_init = bottle.Bottle.__init__

    def patched_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)

        # ContextVar propagation
        _install_before_request(self)

        # Install hop plugin (Plugin API v2 ― applies to all routes, past & future)
        self.install(_SFTracingPlugin())

        # Exception capture (HTTPError 500 or any uncaught Exception)
        _install_error_handler(self)

        if SF_DEBUG:
            print(
                "[[patch_bottle]] tracing hook + plugin + error handler installed",
                log=False,
            )

    bottle.Bottle.__init__ = patched_init
    bottle.Bottle.__sf_tracing_patched__ = True
