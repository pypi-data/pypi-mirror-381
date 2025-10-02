"""
• SFTracingQuartASGIMiddleware: pulls SAILFISH_TRACING_HEADER into your ContextVar.
• patch_quart(): wraps Quart.__init__, installs middleware and
  redefines .route so that each user-land view emits one NetworkHop.
"""

import asyncio
import inspect
import sysconfig
from functools import lru_cache, wraps
from typing import Any, Callable, Set, Tuple

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code, _unwrap_user_func  # your cached helpers

try:
    import quart
    from quart.app import Quart
    from quart.wrappers import Response
except ImportError:
    # Quart not installed → no-op
    def patch_quart():
        return

else:
    # ──────────────────────────────────────────────────────────
    # 1) ASGI middleware to preserve SAILFISH_TRACING_HEADER in ContextVar
    # ──────────────────────────────────────────────────────────
    class SFTracingQuartASGIMiddleware:
        """Wraps the ASGI app so inbound SAILFISH_TRACING_HEADER → ContextVar."""

        def __init__(self, app):
            self.app = app

        async def __call__(self, scope, receive, send):
            if scope.get("type") == "http":
                for name, val in scope.get("headers", []):
                    if name.decode("utf-8").lower() == SAILFISH_TRACING_HEADER.lower():
                        get_or_set_sf_trace_id(
                            val.decode("utf-8"), is_associated_with_inbound_request=True
                        )
                        break
            await self.app(scope, receive, send)

    # ──────────────────────────────────────────────────────────
    # 2) Monkey-patch Quart to install our middleware + route wrapper
    # ──────────────────────────────────────────────────────────
    def patch_quart():
        """
        Patches Quart.__init__ so that:
        1. the internal ASGI app is wrapped by SFTracingQuartASGIMiddleware
            (captures inbound SAILFISH_TRACING_HEADER);
        2. every @app.route handler is wrapped to emit one NetworkHop *and*
            funnel **all** exceptions—*including* quart.exceptions.HTTPException—
            through custom_excepthook, then re-raise so Quart still returns the
            correct HTTP response.
        """

        original_init = Quart.__init__

        def patched_init(self, *args, **kwargs):
            # 1) call original ctor
            original_init(self, *args, **kwargs)

            # 2) wrap ASGI app for header propagation
            self.asgi_app = SFTracingQuartASGIMiddleware(self.asgi_app)

            # 3) patch .route decorator
            original_route = self.route

            def tracing_route(self, rule: str, **options):
                """
                Replacement for @app.route(...) → decorator(fn).
                """
                decorator = original_route(rule, **options)

                def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
                    # unwrap any decorators/closures to find real user fn
                    user_fn = _unwrap_user_func(fn)

                    code = getattr(user_fn, "__code__", None)
                    if not code or not _is_user_code(code.co_filename):
                        return decorator(fn)  # non-user code → no hop/exception capture

                    if getattr(user_fn, "__module__", "").startswith("strawberry"):
                        return decorator(fn)  # skip Strawberry views

                    filename = code.co_filename
                    line_no = code.co_firstlineno
                    name = user_fn.__name__
                    sent: Set[Tuple[str, int]] = set()  # one-time hop flag

                    # choose async vs sync wrapper based on endpoint type
                    if asyncio.iscoroutinefunction(fn):

                        @wraps(fn)
                        async def wrapped(*a, **k):
                            key = (filename, line_no)
                            if key not in sent:
                                _, session_id = get_or_set_sf_trace_id()
                                NetworkHopsTransmitter().send(
                                    session_id=session_id,
                                    line=str(line_no),
                                    column="0",
                                    name=name,
                                    entrypoint=filename,
                                )
                                sent.add(key)
                            try:
                                return await fn(*a, **k)
                            except (
                                Exception
                            ) as exc:  # capture ALL exceptions, incl. HTTPException
                                custom_excepthook(type(exc), exc, exc.__traceback__)
                                raise

                        wrapped_fn = wrapped
                    else:

                        @wraps(fn)
                        def wrapped(*a, **k):
                            key = (filename, line_no)
                            if key not in sent:
                                _, session_id = get_or_set_sf_trace_id()
                                NetworkHopsTransmitter().send(
                                    session_id=session_id,
                                    line=str(line_no),
                                    column="0",
                                    name=name,
                                    entrypoint=filename,
                                )
                                sent.add(key)
                            try:
                                return fn(*a, **k)
                            except Exception as exc:
                                custom_excepthook(type(exc), exc, exc.__traceback__)
                                raise

                        wrapped_fn = wrapped

                    return decorator(wrapped_fn)

                return wrapper

            # rebind the instance's route method
            self.route = tracing_route.__get__(self, Quart)

        # apply the patch once
        Quart.__init__ = patched_init

    # expose the patch function
    __all__ = ["patch_quart"]
