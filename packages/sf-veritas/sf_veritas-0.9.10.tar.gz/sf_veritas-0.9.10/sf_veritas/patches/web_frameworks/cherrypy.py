"""
• Header propagation via Application.__call__               (unchanged).
• Global CherryPy Tool (‘before_handler') → 1 NetworkHop    (fixed).
"""

import inspect
import types
from typing import Any, Callable, Iterable, Set

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook  # ← NEW
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code

# ------------------------------------------------------------------ #
#  Robust un-wrapper (handles LateParamPageHandler, etc.)
# ------------------------------------------------------------------ #
_ATTR_CANDIDATES: Iterable[str] = (
    "resolver",
    "func",
    "python_func",
    "_resolver",
    "wrapped_func",
    "__func",
    "callable",  # CherryPy handlers
)


def _unwrap_user_func(fn: Callable[..., Any]) -> Callable[..., Any]:
    """
    Walk through the layers of wrappers/decorators/handler objects around *fn*
    and return the first plain Python *function* object that:
        • lives in user-land code (per _is_user_code)
        • has a real __code__ object.
    The search is breadth-first and robust to cyclic references.
    """
    seen: Set[int] = set()
    queue = [fn]

    while queue:
        current = queue.pop()
        cid = id(current)
        if cid in seen:
            continue
        seen.add(cid)

        # ── 1. Bound methods (types.MethodType) ──────────────────────────
        # CherryPy's LateParamPageHandler.callable is usually a bound method.
        if isinstance(current, types.MethodType):
            queue.append(current.__func__)
            continue  # don't inspect the MethodType itself any further

        # ── 2. Plain user function?  ─────────────────────────────────────
        if inspect.isfunction(current) and _is_user_code(
            getattr(current.__code__, "co_filename", "")
        ):
            return current

        # ── 3. CherryPy PageHandler exposes `.callable` ──────────────────
        target = getattr(current, "callable", None)
        if callable(target):
            queue.append(target)

        # ── 4. functools.wraps chain (`__wrapped__`) ─────────────────────
        wrapped = getattr(current, "__wrapped__", None)
        if callable(wrapped):
            queue.append(wrapped)

        # ── 5. Other common wrapper attributes ───────────────────────────
        for attr in _ATTR_CANDIDATES:
            val = getattr(current, attr, None)
            if callable(val):
                queue.append(val)

        # ── 6. Objects with a user-defined __call__ method ───────────────
        call_attr = getattr(current, "__call__", None)
        if (
            callable(call_attr)
            and inspect.isfunction(call_attr)
            and _is_user_code(getattr(call_attr.__code__, "co_filename", ""))
        ):
            queue.append(call_attr)

        # ── 7. Closure cells inside functions / inner scopes ─────────────
        code_obj = getattr(current, "__code__", None)
        clos = getattr(current, "__closure__", None)
        if code_obj and clos:
            for cell in clos:
                cell_val = cell.cell_contents
                if callable(cell_val):
                    queue.append(cell_val)

    # Fallback: return the original callable (likely framework code)
    return fn


# 2b.  Exception-capture tool  (runs *after* an error is detected)
def _exception_capture_tool():
    """
    CherryPy calls the ‘before_error_response' hook whenever it is about to
    finalise an error page, regardless of whether the error is a framework
    HTTPError/HTTPRedirect or an uncaught Python exception.
    We tap that hook and forward the traceback to Sailfish.
    """
    import sys

    exc_type, exc_value, exc_tb = sys.exc_info()
    if exc_value:
        if SF_DEBUG:
            print(
                f"[[SFTracingCherryPy]] captured exception: {exc_value!r}",
                log=False,
            )
        custom_excepthook(exc_type, exc_value, exc_tb)


# ------------------------------------------------------------------ #
#  Main patch entry-point
# ------------------------------------------------------------------ #
def patch_cherrypy():
    """
    • Propagate SAILFISH_TRACING_HEADER header → ContextVar.
    • Emit one NetworkHop for the first *user* handler frame in each request.
    • Capture **all** CherryPy exceptions (HTTPError, HTTPRedirect, uncaught
      Python errors) and forward them to `custom_excepthook`.
    """
    try:
        import cherrypy  # CherryPy may not be installed
    except ImportError:
        return

    # ──────────────────────────────────────────────────────────────────
    # 1.  Header propagation – monkey-patch Application.__call__
    # ──────────────────────────────────────────────────────────────────
    env_key = "HTTP_" + SAILFISH_TRACING_HEADER.upper().replace("-", "_")
    if not getattr(cherrypy.Application, "__sf_hdr_patched__", False):
        orig_call = cherrypy.Application.__call__

        def patched_call(self, environ, start_response):
            hdr = environ.get(env_key)
            if hdr:
                get_or_set_sf_trace_id(hdr, is_associated_with_inbound_request=True)
            return orig_call(self, environ, start_response)

        cherrypy.Application.__call__ = patched_call
        cherrypy.Application.__sf_hdr_patched__ = True

    # ──────────────────────────────────────────────────────────────────
    # 2a.  Network-hop tool  (runs before each handler)
    # ──────────────────────────────────────────────────────────────────
    def _network_hop_tool():
        req = cherrypy.serving.request  # thread-local current request
        handler = getattr(req, "handler", None)
        if not callable(handler):
            return

        real_fn = _unwrap_user_func(handler)
        # Skip GraphQL (Strawberry) or non-user code
        if real_fn.__module__.startswith("strawberry"):
            return
        code = getattr(real_fn, "__code__", None)
        if not code or not _is_user_code(code.co_filename):
            return

        hop_key = (code.co_filename, code.co_firstlineno)
        sent = getattr(req, "_sf_hops_sent", set())
        if hop_key in sent:
            return

        _, session_id = get_or_set_sf_trace_id()
        if SF_DEBUG:
            print(
                f"[[SFTracingCherryPy]] hop → {real_fn.__name__} "
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
        sent.add(hop_key)
        req._sf_hops_sent = sent

    if not hasattr(cherrypy.tools, "sf_network_hop"):
        cherrypy.tools.sf_network_hop = cherrypy.Tool(
            "before_handler", _network_hop_tool, priority=5
        )

    # ──────────────────────────────────────────────────────────────────
    # 2b.  Exception-capture tool  (runs before error response)
    # ──────────────────────────────────────────────────────────────────
    def _exception_capture_tool():
        import sys

        exc_type, exc_value, exc_tb = sys.exc_info()
        if exc_value:
            if SF_DEBUG:
                print(
                    f"[[SFTracingCherryPy]] captured exception: {exc_value!r}",
                    log=False,
                )
            custom_excepthook(exc_type, exc_value, exc_tb)

    if not hasattr(cherrypy.tools, "sf_exception_capture"):
        cherrypy.tools.sf_exception_capture = cherrypy.Tool(
            "before_error_response", _exception_capture_tool, priority=100
        )

    # ──────────────────────────────────────────────────────────────────
    # 3.  Enable both tools globally
    # ──────────────────────────────────────────────────────────────────
    cherrypy.config.update(
        {
            "tools.sf_network_hop.on": True,
            "tools.sf_exception_capture.on": True,
        }
    )

    # ──────────────────────────────────────────────────────────────────
    # 4️⃣  Ensure every new Application inherits the tool settings
    # ──────────────────────────────────────────────────────────────────
    if not getattr(cherrypy.Application, "__sf_app_patched__", False):
        orig_app_init = cherrypy.Application.__init__

        def patched_app_init(self, root, script_name="", config=None):
            config = config or {}
            root_conf = config.setdefault("/", {})
            root_conf.setdefault("tools.sf_network_hop.on", True)
            root_conf.setdefault("tools.sf_exception_capture.on", True)
            orig_app_init(self, root, script_name, config)

        cherrypy.Application.__init__ = patched_app_init
        cherrypy.Application.__sf_app_patched__ = True

    if SF_DEBUG:
        print(
            "[[patch_cherrypy]] NetworkHop & Exception tools globally enabled",
            log=False,
        )
