"""
Adds:
• before_request hook → ContextVar propagation (unchanged).
• global add_url_rule / Blueprint.add_url_rule patch →
  wraps every endpoint in a hop-emitting closure.
"""

from functools import wraps
from types import MethodType
from typing import Callable, Set, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id

# ────────────────────────────────────────────────────────────────
#   shared helpers
# ────────────────────────────────────────────────────────────────
from .utils import _is_user_code, _unwrap_user_func  # cached helpers


def _make_hop_wrapper(
    fn: Callable, hop_key: Tuple[str, int], fn_name: str, filename: str
):
    """
    Return a wrapper that sends a NetworkHop exactly once per request.
    Uses flask.g to remember which hops have fired.
    """
    from flask import g

    @wraps(fn)
    def _wrapped(*args, **kwargs):  # noqa: ANN001
        _, session_id = get_or_set_sf_trace_id()

        sent: Set[Tuple[str, int]] = getattr(g, "_sf_hops_sent", set())
        if hop_key not in sent:
            if SF_DEBUG:
                print(
                    f"[[SFTracingFlask]] hop → {fn_name} ({filename}:{hop_key[1]}) "
                    f"session={session_id}",
                    log=False,
                )

            NetworkHopsTransmitter().send(
                session_id=session_id,
                line=str(hop_key[1]),
                column="0",
                name=fn_name,
                entrypoint=filename,
            )
            sent.add(hop_key)
            g._sf_hops_sent = sent

        return fn(*args, **kwargs)

    return _wrapped


def _wrap_if_user_view(endpoint_fn: Callable):
    """
    Decide whether to wrap `endpoint_fn`. Returns the (possibly wrapped)
    callable.  Suppress wrapping for library code or Strawberry handlers.
    """
    real_fn = _unwrap_user_func(endpoint_fn)

    # Skip Strawberry GraphQL views – Strawberry extension owns them
    if real_fn.__module__.startswith("strawberry"):
        return endpoint_fn

    code = getattr(real_fn, "__code__", None)
    if not code or not _is_user_code(code.co_filename):
        return endpoint_fn

    hop_key = (code.co_filename, code.co_firstlineno)
    return _make_hop_wrapper(endpoint_fn, hop_key, real_fn.__name__, code.co_filename)


# ────────────────────────────────────────────────────────────────
#   Context-propagation (unchanged)
# ────────────────────────────────────────────────────────────────
def _install_before_request(app):
    from flask import request

    @app.before_request
    def _extract_sf_trace():
        hdr = request.headers.get(SAILFISH_TRACING_HEADER)
        if hdr:
            get_or_set_sf_trace_id(hdr, is_associated_with_inbound_request=True)


# ────────────────────────────────────────────────────────────────
#   Monkey-patch Flask & Blueprint
# ────────────────────────────────────────────────────────────────
try:
    import flask
    from flask import Blueprint

    def _patch_add_url_rule(cls):
        """
        Patch *cls*.add_url_rule (cls is Flask or Blueprint) so the final
        stored view function is wrapped after Flask registers it.  Works for:
            • view_func positional
            • endpoint string lookup
            • CBV's as_view()
        """
        original_add = cls.add_url_rule

        def patched_add(
            self, rule, endpoint=None, view_func=None, **options
        ):  # noqa: ANN001
            # 1. Let Flask register the route first
            original_add(self, rule, endpoint=endpoint, view_func=view_func, **options)

            # 2. Resolve the canonical endpoint name
            ep_name = endpoint or (view_func and view_func.__name__)
            if not ep_name:
                return  # should not happen, but be safe

            target = self.view_functions.get(ep_name)
            if not callable(target):
                return

            # 3. Wrap if user code
            wrapped = _wrap_if_user_view(target)
            self.view_functions[ep_name] = wrapped

        cls.add_url_rule = patched_add

    def patch_flask():
        """
        • Installs before_request header propagation
        • Wraps every endpoint to emit a single NetworkHop
        • **NEW:** patches Flask.handle_exception + handle_user_exception so ANY
        exception—including flask.abort / HTTPException—triggers custom_excepthook.
        """
        if getattr(flask.Flask, "__sf_tracing_patched__", False):
            return  # idempotent

        # --- 1. Patch Flask.__init__ to add before_request every time -----------
        original_flask_init = flask.Flask.__init__

        def patched_init(self, *args, **kwargs):
            original_flask_init(self, *args, **kwargs)
            _install_before_request(self)

        flask.Flask.__init__ = patched_init

        # --- 2. Patch add_url_rule for both Flask and Blueprint -----------------
        _patch_add_url_rule(flask.Flask)
        _patch_add_url_rule(Blueprint)

        # --- 3. Patch exception handlers once on the class ----------------------
        _mw_path = "sf_veritas_exception_patch_applied"
        if not getattr(flask.Flask, _mw_path, False):
            orig_handle_exc = flask.Flask.handle_exception
            orig_handle_user_exc = flask.Flask.handle_user_exception

            def _patched_handle_exception(self, e):
                custom_excepthook(type(e), e, e.__traceback__)
                return orig_handle_exc(self, e)

            def _patched_handle_user_exception(self, e):
                custom_excepthook(type(e), e, e.__traceback__)
                return orig_handle_user_exc(self, e)

            flask.Flask.handle_exception = _patched_handle_exception  # 500 errors
            flask.Flask.handle_user_exception = (
                _patched_handle_user_exception  # HTTPExc.
            )

            setattr(flask.Flask, _mw_path, True)

        flask.Flask.__sf_tracing_patched__ = True

        if SF_DEBUG:
            print(
                "[[patch_flask]] tracing hooks + exception capture installed", log=False
            )

except ImportError:  # Flask not installed

    def patch_flask():  # noqa: D401
        """No-op when Flask is absent."""
        return
