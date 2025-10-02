import inspect
import sys
import sysconfig
from functools import lru_cache
from typing import Any, Callable, Set, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code  # cached helpers


# ------------------------------------------------------------------ #
# 1.2 Tween factory: header + one-shot profile tracer + exceptions   #
# ------------------------------------------------------------------ #
def _sf_tracing_tween_factory(handler, registry):
    """
    Pyramid tween that:
      • Reads SAILFISH_TRACING_HEADER header → ContextVar.
      • Sets a one-shot profiler to emit the first user-land NetworkHop.
      • Funnels *all* exceptions (including HTTPException) through
        `custom_excepthook` before letting Pyramid continue normal handling.
    """

    def _tween(request):
        # ── 1) Propagate incoming trace header ──────────────────────────
        hdr = request.headers.get(SAILFISH_TRACING_HEADER)
        if hdr:
            get_or_set_sf_trace_id(hdr, is_associated_with_inbound_request=True)

        # ── 2) One-shot tracer to detect first user-code frame ──────────
        def tracer(frame, event, _arg):
            if event != "call":  # only Python calls
                return tracer
            fn_path = frame.f_code.co_filename
            if _is_user_code(fn_path):
                _, session_id = get_or_set_sf_trace_id()
                func_name = frame.f_code.co_name
                line_no = frame.f_lineno
                NetworkHopsTransmitter().send(
                    session_id=session_id,
                    line=str(line_no),
                    column="0",
                    name=func_name,
                    entrypoint=fn_path,
                )
                sys.setprofile(None)  # disable after first hop
                return None
            return tracer

        sys.setprofile(tracer)

        # ── 3) Call downstream handler & capture **all** exceptions ─────
        try:
            return handler(request)
        except Exception as exc:  # HTTPException included
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise  # re-raise for Pyramid
        finally:
            sys.setprofile(None)  # safety-net cleanup

    return _tween


# ------------------------------------------------------------------ #
# 1.3 Monkey-patch Configurator to auto-add our tween               #
# ------------------------------------------------------------------ #
def patch_pyramid():
    """
    Ensure every Pyramid Configurator implicitly registers our tween
    at the INVOCATION stage (just above MAIN).
    """
    try:
        import pyramid.config
        import pyramid.tweens
    except ImportError:
        return  # Pyramid not installed

    original_init = pyramid.config.Configurator.__init__

    def patched_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        # Use a dotted name—implicit ordering places it just above MAIN
        dotted = f"{_sf_tracing_tween_factory.__module__}._sf_tracing_tween_factory"
        # 'over=pyramid.tweens.MAIN' ensures our tween runs *before* the main handler
        self.add_tween(dotted, over=pyramid.tweens.MAIN)

    pyramid.config.Configurator.__init__ = patched_init
