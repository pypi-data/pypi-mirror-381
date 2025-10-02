import functools
import inspect
import sys
import sysconfig
from functools import lru_cache
from typing import Any, Callable, Optional, Set

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from ..constants import supported_network_verbs as HTTP_METHODS
from .utils import _is_user_code, _unwrap_user_func

_stdlib = sysconfig.get_paths()["stdlib"]


@lru_cache(maxsize=512)
def _is_user_code(path: Optional[str]) -> bool:
    """
    True only for “application” files (not stdlib or site-packages).
    """
    if not path or path.startswith("<"):
        return False
    if path.startswith(_stdlib):
        return False
    if "site-packages" in path or "dist-packages" in path:
        return False
    return True


def patch_robyn():
    """
    Monkey-patch robyn.Robyn so that every Robyn() instance
    auto-wraps route handlers with header propagation and network‐hop emission.
    Safe no-op if Robyn isn't installed.
    """
    try:
        import robyn
    except ImportError:
        return

    for method_name in HTTP_METHODS:
        if not hasattr(robyn.Robyn, method_name):
            continue

        original_factory = getattr(robyn.Robyn, method_name)

        def make_patched(factory):
            @functools.wraps(factory)
            def patched(self, path: str, *args, **kwargs):
                # original decorator returned by Robyn
                decorator = factory(self, path, *args, **kwargs)

                def custom_decorator(fn):
                    real_fn = _unwrap_user_func(fn)

                    @functools.wraps(fn)
                    async def wrapped_handler(request, *a, **kw):
                        # ──────────────────────────────────────────────────────────
                        # 1) Capture inbound trace header
                        # ──────────────────────────────────────────────────────────
                        hdr = getattr(request, "headers", {}).get(
                            SAILFISH_TRACING_HEADER
                        )
                        if hdr:
                            get_or_set_sf_trace_id(
                                hdr, is_associated_with_inbound_request=True
                            )

                        # ──────────────────────────────────────────────────────────
                        # 2) Emit a single NetworkHop (user code only)
                        # ──────────────────────────────────────────────────────────
                        filename = real_fn.__code__.co_filename
                        if _is_user_code(filename):
                            line_no = real_fn.__code__.co_firstlineno
                            _, session_id = get_or_set_sf_trace_id()

                            if SF_DEBUG:
                                print(
                                    f"[[RobynHop]] {real_fn.__name__} @ {filename}:{line_no} "
                                    f"session={session_id}",
                                    log=False,
                                )

                            NetworkHopsTransmitter().send(
                                session_id=session_id,
                                line=str(line_no),
                                column="0",
                                name=real_fn.__name__,
                                entrypoint=filename,
                            )

                        # ──────────────────────────────────────────────────────────
                        # 3) Run user handler and funnel ANY exception (including
                        #    robyn.HTTPException) through custom_excepthook
                        # ──────────────────────────────────────────────────────────
                        try:
                            return await real_fn(request, *a, **kw)
                        except Exception as exc:  # noqa: BLE001
                            # Fast path: let custom_excepthook decide deduplication
                            custom_excepthook(type(exc), exc, exc.__traceback__)
                            raise  # Re-raise so Robyn still returns proper error

                    # Register wrapped_handler in place of the original
                    return decorator(wrapped_handler)

                return custom_decorator

            return patched

        # bind a fresh patched_factory for each HTTP method
        setattr(robyn.Robyn, method_name, make_patched(original_factory))
