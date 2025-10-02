"""
Context-propagation + user-code NetworkHop emission for every aiohttp
request, while skipping Strawberry GraphQL views.
"""

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id

# ------------------------------------------------------------------ #
# shared helpers
# ------------------------------------------------------------------ #
from .utils import _is_user_code, _unwrap_user_func  # cached


# ------------------------------------------------------------------ #
# monkey-patch
# ------------------------------------------------------------------ #
def patch_aiohttp():
    """
    • prepend a middleware that propagates SAILFISH_TRACING_HEADER _and_
      emits a single NetworkHop for user handlers;
    • patch Application.add_route(s) so every future handler
      goes through the wrapper (works for RouteTableDef too).
    Safe no-op if aiohttp isn't installed.
    """
    try:
        from aiohttp import web
    except ImportError:  # aiohttp missing
        return

    # ===========================================================
    # 1 | Middleware  (1 ContextVar; 2 Hop emission)
    # ===========================================================
    @web.middleware
    async def _sf_tracing_middleware(request: web.Request, handler):
        """
        1 - Seed ContextVar from the inbound SAILFISH_TRACING_HEADER header.
        2 - Emit exactly one NetworkHop per user handler.
        3 - Capture *all* exceptions—including aiohttp.web.HTTPException—and
        route them through `custom_excepthook` before letting aiohttp
        continue its normal error handling.
        """
        # 1. Trace-id propagation
        incoming = request.headers.get(SAILFISH_TRACING_HEADER)
        if incoming:
            get_or_set_sf_trace_id(incoming, is_associated_with_inbound_request=True)

        # 2. Hop emission (same logic as before)
        real_fn = _unwrap_user_func(handler)
        if callable(real_fn) and not real_fn.__module__.startswith("strawberry"):
            code = getattr(real_fn, "__code__", None)
            if code and _is_user_code(code.co_filename):
                key = (code.co_filename, code.co_firstlineno)
                sent = request.setdefault("sf_hops_sent", set())
                if key not in sent:
                    _, session_id = get_or_set_sf_trace_id()
                    if SF_DEBUG:
                        print(
                            f"[[AiohttpHop]] → {real_fn.__name__} "
                            f"({code.co_filename}:{code.co_firstlineno}) "
                            f"session={session_id}",
                            log=False,
                        )
                    NetworkHopsTransmitter().send(
                        session_id=session_id,
                        line=str(code.co_firstlineno),
                        column="0",
                        name=real_fn.__name__,
                        entrypoint=code.co_filename,
                    )
                    sent.add(key)

        # 3. Exception capture
        try:
            return await handler(request)
        except Exception as exc:  # ← captures *all* errors
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise  # re-raise for aiohttp

    # ===========================================================
    # 2 | Patch Application.__init__ to insert middleware
    # ===========================================================
    original_init = web.Application.__init__

    def patched_init(self, *args, middlewares=None, **kwargs):
        mlist = list(middlewares or [])
        mlist.insert(0, _sf_tracing_middleware)  # prepend → runs first
        original_init(self, *args, middlewares=mlist, **kwargs)
        _patch_router(self.router)  # apply once per app

    web.Application.__init__ = patched_init

    # ===========================================================
    # 3 | Patch router.add_route / add_routes for future calls
    # ===========================================================
    def _patch_router(router):
        if getattr(router, "_sf_tracing_patched", False):
            return  # already done

        orig_add_route = router.add_route
        orig_add_routes = router.add_routes

        def _wrap_and_add(method, path, handler, *a, **kw):  # noqa: ANN001
            return orig_add_route(method, path, _wrap_handler(handler), *a, **kw)

        def _wrap_handler(h):
            # strawberry skip & user-code check happen in middleware,
            # but wrapping here avoids duplicate stack frames
            return _unwrap_user_func(h) or h

        def _new_add_routes(routes):
            wrapped = [
                (
                    (m, p, _wrap_handler(h), *rest)  # route is (method,path,handler,…)
                    if len(r) >= 3
                    else r
                )
                for r in routes
                for (m, p, h, *rest) in (r,)  # unpack safely
            ]
            return orig_add_routes(wrapped)

        router.add_route = _wrap_and_add
        router.add_routes = _new_add_routes
        router._sf_tracing_patched = True
        if SF_DEBUG:
            print("[[patch_aiohttp]] router hooks installed", log=False)

    if SF_DEBUG:
        print("[[patch_aiohttp]] middleware + init patch applied", log=False)
