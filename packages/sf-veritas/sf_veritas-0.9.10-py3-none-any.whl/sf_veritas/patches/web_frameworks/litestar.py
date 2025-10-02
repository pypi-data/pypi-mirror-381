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


def _sf_tracing_factory(app: Callable) -> Callable:
    """
    ASGI middleware that
      • propagates the inbound SAILFISH_TRACING_HEADER header, and
      • reports any unhandled exception via `custom_excepthook`.
    """

    async def _middleware(scope, receive, send):
        # Header propagation
        if scope.get("type") == "http":
            for name, val in scope.get("headers", []):
                if name.decode().lower() == SAILFISH_TRACING_HEADER.lower():
                    get_or_set_sf_trace_id(
                        val.decode(), is_associated_with_inbound_request=True
                    )
                    break
        # Exception capture
        try:
            await app(scope, receive, send)
        except Exception as exc:  # noqa: BLE001
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise

    return _middleware


def _sf_profile_factory(app: Callable) -> Callable:
    """
    ASGI middleware that installs a one-shot profiler tracer to fire on the
    first user-land Python call, then disables itself.  Emits exactly one
    NetworkHop per request.
    """

    def _make_tracer():
        def tracer(frame, event, _arg):
            try:
                # Skip any C-level events instantly
                if event.startswith("c_"):
                    return None

                # Only care about the first Python call into user code
                if event == "call" and _is_user_code(frame.f_code.co_filename):
                    _, session_id = get_or_set_sf_trace_id()

                    func_name = frame.f_code.co_name
                    line_no = frame.f_lineno
                    filename = frame.f_code.co_filename

                    if SF_DEBUG:
                        print(
                            f"[[LitestarProfile]] SEND → {func_name} "
                            f"({filename}:{line_no}) session={session_id}",
                            log=False,
                        )

                    try:
                        NetworkHopsTransmitter().send(
                            session_id=session_id,
                            line=str(line_no),
                            column="0",
                            name=func_name,
                            entrypoint=filename,
                        )
                    except Exception as send_err:
                        # Log send errors but don't break the request
                        print(
                            "[[LitestarProfile ERROR send]]", repr(send_err), log=False
                        )
                    finally:
                        # Turn off profiling immediately
                        sys.setprofile(None)

                    return None

                return tracer
            except Exception as err:
                # Any tracer error → disable profiling & log it
                sys.setprofile(None)
                print("[[LitestarProfile ERROR tracer]]", repr(err), log=False)
                return None

        return tracer

    class _ProfileMiddleware:
        def __init__(self, app: Callable):
            self.app = app

        async def __call__(self, scope, receive, send):
            if scope.get("type") == "http":
                # Install the one-shot tracer
                sys.setprofile(_make_tracer())
                try:
                    await self.app(scope, receive, send)
                except Exception as exc:  # noqa: BLE001
                    custom_excepthook(type(exc), exc, exc.__traceback__)
                    raise
                finally:
                    sys.setprofile(None)
            else:
                try:
                    await self.app(scope, receive, send)
                except Exception as exc:  # noqa: BLE001
                    custom_excepthook(type(exc), exc, exc.__traceback__)
                    raise

    return _ProfileMiddleware(app)


def patch_litestar() -> None:
    """
    Monkey-patch Litestar.__init__ so every instance auto-wraps with:
      1) _sf_tracing_factory → inbound trace-header propagation
      2) _sf_profile_factory → one-shot tracer for NetworkHops
    Safe no-op if Litestar is not installed.
    """
    try:
        import litestar
        from litestar import Litestar
        from litestar.middleware import DefineMiddleware
    except ImportError:
        return

    original_init = Litestar.__init__

    # ---------------------------------------------------------------------------
    # UPDATED patched_init in patch_litestar.py  (entire function shown)
    # ---------------------------------------------------------------------------
    def patched_init(self, *args, **kwargs):
        """
        Injects Sailfish into every Litestar app instance by

        1. Pre-pending two ASGI middlewares
        • _sf_tracing_factory  – header propagation + last-chance catcher
        • _sf_profile_factory  – one-shot hop emitter
        2. Adding a **generic exception handler** so *any* exception—
        including `HTTPException` and framework-level errors—triggers
        `custom_excepthook` exactly once before Litestar builds the
        response.
        """

        # ---------------------------------------------------------- #
        # 1 | Middleware injection (existing behaviour)
        # ---------------------------------------------------------- #
        mw = list(kwargs.get("middleware", []))
        from litestar.middleware import DefineMiddleware

        mw.insert(0, DefineMiddleware(_sf_tracing_factory))
        mw.insert(1, DefineMiddleware(_sf_profile_factory))
        kwargs["middleware"] = mw

        # ---------------------------------------------------------- #
        # 2 | Universal exception handler
        # ---------------------------------------------------------- #
        def _sf_exception_handler(request, exc):  # type: ignore[valid-type]
            """
            Litestar calls this for **any** Exception once routing / dep-
            resolution is done. We just forward to `custom_excepthook`
            and re-raise so the builtin handler still produces a Response.
            """
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise exc  # let Litestar fall back to its default logic

        # Merge with user-supplied handlers (if any)
        existing_handlers = kwargs.get("exception_handlers", {})
        if isinstance(existing_handlers, dict):
            existing_handlers.setdefault(Exception, _sf_exception_handler)
        else:  # Litestar also accepts list[tuple[Exception, Handler]]
            existing_handlers = list(existing_handlers)  # type: ignore[arg-type]
            existing_handlers.append((Exception, _sf_exception_handler))
        kwargs["exception_handlers"] = existing_handlers

        # ---------------------------------------------------------- #
        # 3 | Debug log
        # ---------------------------------------------------------- #
        if SF_DEBUG:
            print(
                "[[patch_litestar]] installed header+profile middleware AND "
                "global exception handler",
                log=False,
            )

        # ---------------------------------------------------------- #
        # 4 | Delegate to original __init__
        # ---------------------------------------------------------- #
        return original_init(self, *args, **kwargs)

    Litestar.__init__ = patched_init
