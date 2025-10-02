import inspect
import sys
import sysconfig
from functools import lru_cache, wraps
from typing import Any, Callable, Optional, Set, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import PRINT_CONFIGURATION_STATUSES, SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _unwrap_user_func

# ────────────────────────────────────────────────────
# User-code predicate: skip stdlib & site-packages
# ────────────────────────────────────────────────────
_STDLIB = sysconfig.get_paths()["stdlib"]
_SITE_TAGS = ("site-packages", "dist-packages")
_SKIP_PREFIXES = (_STDLIB, "/usr/local/lib/python", "/usr/lib/python")


@lru_cache(maxsize=512)
def _is_user_code(path: Optional[str] = None) -> bool:
    """True only for your application files."""
    if not path or path.startswith("<"):
        return False
    for p in _SKIP_PREFIXES:
        if path.startswith(p):
            return False
    return not any(tag in path for tag in _SITE_TAGS)


# ────────────────────────────────────────────────────
# Patch AsyncConsumer.__call__ to hook connect + receive
# ────────────────────────────────────────────────────
def patch_async_consumer_call():
    """
    Wraps AsyncConsumer.__call__ so that for each HTTP or WebSocket
    connection:
      1) SAILFISH_TRACING_HEADER → ContextVar
      2) Emit a NetworkHop at first user frame in websocket_connect
      3) Dynamically wrap websocket_receive to emit a hop on first message
      4) Forward any exception to custom_excepthook
    """
    try:
        from channels.consumer import AsyncConsumer  # type: ignore

        orig_call = AsyncConsumer.__call__
    except:
        if PRINT_CONFIGURATION_STATUSES:
            print("Channels AsyncConsumer not found; skipping patch", log=False)
        return

    if PRINT_CONFIGURATION_STATUSES:
        print("Patching AsyncConsumer.__call__ for NetworkHops", log=False)

    @wraps(orig_call)
    async def custom_call(self, scope, receive, send):
        # — Propagate header into ContextVar —
        header_val = None
        if scope["type"] in ("http", "websocket"):
            for name, val in scope.get("headers", []):
                if name.lower() == SAILFISH_TRACING_HEADER.lower().encode():
                    header_val = val.decode("utf-8")
                    break
        get_or_set_sf_trace_id(header_val, is_associated_with_inbound_request=True)

        # — One-shot profiler for websocket_connect inside orig_call —
        def tracer(frame, event, _arg):
            if event == "call":
                fn_path = frame.f_code.co_filename
                if _is_user_code(fn_path):
                    _, session = get_or_set_sf_trace_id()
                    NetworkHopsTransmitter().send(
                        session_id=session,
                        line=str(frame.f_lineno),
                        column="0",
                        name=frame.f_code.co_name,
                        entrypoint=fn_path,
                    )
                    sys.setprofile(None)
                    return None
            return tracer

        sys.setprofile(tracer)

        # — Dynamically wrap this instance's websocket_receive —
        recv = getattr(self, "websocket_receive", None)
        if recv and hasattr(self, "websocket_receive"):

            @wraps(recv)
            async def wrapped_receive(event):
                # Emit first user-frame hop inside receive
                def recv_tracer(fr, ev, _a):
                    if ev == "call":
                        path = fr.f_code.co_filename
                        if _is_user_code(path):
                            _, sess = get_or_set_sf_trace_id()
                            NetworkHopsTransmitter().send(
                                session_id=sess,
                                line=str(fr.f_lineno),
                                column="0",
                                name=fr.f_code.co_name,
                                entrypoint=path,
                            )
                            sys.setprofile(None)
                            return None
                    return recv_tracer

                sys.setprofile(recv_tracer)
                try:
                    return await recv(event)
                finally:
                    sys.setprofile(None)

            # override on this instance only
            setattr(self, "websocket_receive", wrapped_receive)

        # — Call through to original (handles connect, receive, disconnect) —
        try:
            await orig_call(self, scope, receive, send)
        except Exception as exc:
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise
        finally:
            sys.setprofile(None)

    # Apply the patch
    AsyncConsumer.__call__ = custom_call

    if PRINT_CONFIGURATION_STATUSES:
        print("AsyncConsumer.__call__ patched successfully", log=False)
