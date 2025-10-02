import inspect
import site
import sysconfig
from functools import lru_cache
from typing import Any, Callable, Set, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code, _unwrap_user_func


def patch_tornado():
    """
    Monkey-patch tornado.web.RequestHandler so that every request:

      1. Propagates SAILFISH_TRACING_HEADER into the ContextVar.
      2. Emits ONE NetworkHop when user-land verb handler starts.
      3. Funnels *all* exceptions—including tornado.web.HTTPError—through
         custom_excepthook before Tornado's own error machinery runs.

    Safe no-op if Tornado isn't installed.
    """
    try:
        import tornado.web
    except ImportError:  # Tornado not installed
        return

    # --------------------------------------------------------------- #
    # a)  Header capture + hop emission (prepare) – unchanged logic
    # --------------------------------------------------------------- #
    original_prepare = tornado.web.RequestHandler.prepare

    def patched_prepare(self, *args, **kwargs):
        # -- 1) Header propagation
        header_val = self.request.headers.get(SAILFISH_TRACING_HEADER)
        if header_val:
            get_or_set_sf_trace_id(header_val, is_associated_with_inbound_request=True)

        # -- 2) Emit hop once per request for the actual HTTP verb handler
        method_name = self.request.method.lower()
        handler_fn = getattr(self, method_name, None)

        if callable(handler_fn):
            module = getattr(handler_fn, "__module__", "")
            if not module.startswith("strawberry"):
                real_fn = _unwrap_user_func(handler_fn)
                code_obj = getattr(real_fn, "__code__", None)
                if code_obj and _is_user_code(code_obj.co_filename):
                    key = (code_obj.co_filename, code_obj.co_firstlineno)
                    if key not in SailfishHandlerPatch._sent:
                        _, session_id = get_or_set_sf_trace_id()
                        if SF_DEBUG:
                            print(
                                f"[[TornadoHop]] {real_fn.__name__} "
                                f"({code_obj.co_filename}:{code_obj.co_firstlineno}) "
                                f"session={session_id}",
                                log=False,
                            )
                        NetworkHopsTransmitter().send(
                            session_id=session_id,
                            line=str(code_obj.co_firstlineno),
                            column="0",
                            name=real_fn.__name__,
                            entrypoint=code_obj.co_filename,
                        )
                        SailfishHandlerPatch._sent.add(key)

        return original_prepare(self, *args, **kwargs)

    tornado.web.RequestHandler.prepare = patched_prepare

    # --------------------------------------------------------------- #
    # b)  Exception capture – patch _execute and write_error
    # --------------------------------------------------------------- #
    original_execute = tornado.web.RequestHandler._execute
    original_write_error = tornado.web.RequestHandler.write_error

    async def patched_execute(self, *args, **kwargs):
        try:
            return await original_execute(self, *args, **kwargs)
        except Exception as exc:  # HTTPError included
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise  # let Tornado handle 500/4xx

    def patched_write_error(self, status_code, **kwargs):
        """
        Tornado calls write_error for HTTPError and uncaught exceptions.
        Capture the exception (when provided) before rendering.
        """
        exc_info = kwargs.get("exc_info")
        if exc_info and isinstance(exc_info, tuple) and exc_info[1]:
            exc_type, exc_val, exc_tb = exc_info
            custom_excepthook(exc_type, exc_val, exc_tb)
        # Fallback: still call original renderer
        return original_write_error(self, status_code, **kwargs)

    tornado.web.RequestHandler._execute = patched_execute
    tornado.web.RequestHandler.write_error = patched_write_error


class SailfishHandlerPatch:
    """
    Helper to hold our per-request dedupe set.
    We clear this once per IOLoop iteration via on_finish().
    """

    _sent: Set[Tuple[str, int]] = set()

    @staticmethod
    def clear_sent():
        SailfishHandlerPatch._sent.clear()


# Hook into on_finish to reset dedupe for the next request
try:
    import tornado.web

    original_on_finish = tornado.web.RequestHandler.on_finish

    def patched_on_finish(self):
        SailfishHandlerPatch.clear_sent()
        return original_on_finish(self)

    tornado.web.RequestHandler.on_finish = patched_on_finish
except ImportError:
    pass
