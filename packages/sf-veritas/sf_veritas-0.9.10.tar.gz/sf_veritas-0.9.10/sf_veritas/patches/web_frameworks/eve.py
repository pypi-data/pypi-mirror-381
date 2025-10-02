from functools import wraps
from typing import Callable, Set, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code, _unwrap_user_func  # shared helpers


# ──────────────────────────────────────────────────────────────
# Header propagation  (still one before_request handler)
# ──────────────────────────────────────────────────────────────
def _install_header_middleware(app):
    from flask import request

    @app.before_request
    def _extract_sf_header():
        rid = request.headers.get(SAILFISH_TRACING_HEADER)
        if rid:
            get_or_set_sf_trace_id(rid, is_associated_with_inbound_request=True)


# ──────────────────────────────────────────────────────────────
# Per-view hop wrapper
# ──────────────────────────────────────────────────────────────
def _hop_wrapper(view_fn: Callable):
    """
    Return a wrapped callable that fires NetworkHopsTransmitter.send()
    once per request (de-duped via flask.g).
    """
    from flask import g

    real_fn = _unwrap_user_func(view_fn)

    # Skip Strawberry handlers – handled by Strawberry extension
    if real_fn.__module__.startswith("strawberry"):
        return view_fn

    code = getattr(real_fn, "__code__", None)
    if not code or not _is_user_code(code.co_filename):
        return view_fn

    hop_key = (code.co_filename, code.co_firstlineno)
    fn_name = real_fn.__name__
    filename = code.co_filename
    line_no = code.co_firstlineno

    @wraps(view_fn)
    def _wrapped(*args, **kwargs):
        _, session_id = get_or_set_sf_trace_id()

        sent: Set[Tuple[str, int]] = getattr(g, "_sf_hops_sent", set())
        if hop_key not in sent:
            if SF_DEBUG:
                print(
                    f"[[SFTracingEve]] hop → {fn_name} "
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
            g._sf_hops_sent = sent

        return view_fn(*args, **kwargs)

    return _wrapped


def _patch_add_url_rule(cls):
    """
    Patch add_url_rule on *cls* (cls is Eve or Blueprint) so that the final
    stored endpoint function is wrapped *after* Flask has done its own
    bookkeeping.  This catches:
      • Eve resource endpoints created internally via register_resource()
      • Manual @app.route() decorators
      • Blueprints, CBVs, etc.
    """
    original_add = cls.add_url_rule

    def patched_add(
        self, rule, endpoint=None, view_func=None, **options
    ):  # noqa: ANN001
        # let Eve/Flask register the route first
        original_add(self, rule, endpoint=endpoint, view_func=view_func, **options)

        ep = endpoint or (view_func and view_func.__name__)
        if not ep:  # defensive
            return

        target = self.view_functions.get(ep)
        if callable(target):
            self.view_functions[ep] = _hop_wrapper(target)

    cls.add_url_rule = patched_add


# ──────────────────────────────────────────────────────────────
# Public entry-point
# ──────────────────────────────────────────────────────────────
def patch_eve():
    """
    • Adds ContextVar propagation middleware
    • Wraps every Eve endpoint (and Blueprint endpoints) to emit one hop
    """
    try:
        import eve
        from flask import Blueprint  # Eve relies on Flask blueprints
    except ImportError:
        return

    # Guard against double-patching
    if getattr(eve.Eve, "__sf_tracing_patched__", False):
        return

    # 1.  Patch Eve.add_url_rule *and* Blueprint.add_url_rule
    _patch_add_url_rule(eve.Eve)
    _patch_add_url_rule(Blueprint)

    # 2.  Patch Eve.__init__ to install before_request middleware
    original_init = eve.Eve.__init__

    def patched_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        _install_header_middleware(self)

    eve.Eve.__init__ = patched_init
    eve.Eve.__sf_tracing_patched__ = True

    if SF_DEBUG:
        print("[[patch_eve]] header middleware + hop wrapper installed", log=False)
