"""
Context-var propagation  +  first-hop NetworkHop emission.
"""

# ------------------------------------------------------------------ #
# Shared helpers (same as Django/FastAPI utils)
# ------------------------------------------------------------------ #
import inspect
import sysconfig
from functools import lru_cache
from typing import Any, Callable, Optional, Set, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code, _unwrap_user_func


# ------------------------------------------------------------------ #
# Middleware
# ------------------------------------------------------------------ #
async def _sf_tracing_middleware(request, handler):
    """
    BlackSheep function-style middleware that:
    1. Propagates trace-id from SAILFISH_TRACING_HEADER.
    2. Emits one NetworkHop for the first user-land handler.
    3. Captures *any* exception (HTTPException, RuntimeError, etc.),
       passes it to `custom_excepthook`, then re-raises so BlackSheep
       can continue its normal error handling.
    """

    # 1. Header → ContextVar
    raw_hdr = request.headers.get_first(SAILFISH_TRACING_HEADER.encode())
    if raw_hdr:
        try:
            hdr_val = raw_hdr.decode()
        except UnicodeDecodeError:
            hdr_val = str(raw_hdr)
        get_or_set_sf_trace_id(hdr_val, is_associated_with_inbound_request=True)

    # 2. Hop capture (once per request)
    if not getattr(request, "_sf_hop_sent", False):
        user_fn = _unwrap_user_func(handler)
        if (
            inspect.isfunction(user_fn)
            and _is_user_code(user_fn.__code__.co_filename)
            and not user_fn.__module__.startswith("strawberry")
        ):
            filename = user_fn.__code__.co_filename
            line_no = user_fn.__code__.co_firstlineno
            fn_name = user_fn.__name__
            _, session_id = get_or_set_sf_trace_id()

            if SF_DEBUG:
                print(
                    f"[[BlackSheepHop]] {fn_name} ({filename}:{line_no}) "
                    f"session={session_id}",
                    log=False,
                )

            NetworkHopsTransmitter().send(
                session_id=session_id,
                line=str(line_no),
                column="0",
                name=fn_name,
                entrypoint=filename,
            )
        request._sf_hop_sent = True  # mark as done

    # 3. Continue down the chain and capture exceptions
    try:
        return await handler(request)
    except Exception as exc:  # ← includes HTTPException & friends
        custom_excepthook(type(exc), exc, exc.__traceback__)
        raise  # Let BlackSheep build the response


# ------------------------------------------------------------------ #
# Monkey-patch Application.__init__
# ------------------------------------------------------------------ #
def patch_blacksheep():
    """
    Injects the tracing middleware into every BlackSheep Application.
    Safe no-op if BlackSheep isn't installed or already patched.
    """
    try:
        from blacksheep import Application
    except ImportError:
        return

    if getattr(Application, "__sf_tracing_patched__", False):
        return  # already patched

    original_init = Application.__init__

    def patched_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        # Put our middleware first so we run before user middlewares
        self.middlewares.insert(0, _sf_tracing_middleware)

    Application.__init__ = patched_init
    Application.__sf_tracing_patched__ = True

    if SF_DEBUG:
        print("[[patch_blacksheep]] tracing middleware installed", log=False)
