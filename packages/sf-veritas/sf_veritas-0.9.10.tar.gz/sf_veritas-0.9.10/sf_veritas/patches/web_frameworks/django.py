import asyncio
import inspect

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object  # fallback for non-Django environments

from ...constants import SAILFISH_TRACING_HEADER
from ...custom_excepthook import custom_excepthook
from ...env_vars import PRINT_CONFIGURATION_STATUSES, SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id


def find_and_modify_output_wrapper():
    if PRINT_CONFIGURATION_STATUSES:
        print("find_and_modify_output_wrapper", log=False)
    try:
        import django
        import django.core.management.base

        base_path = inspect.getfile(django.core.management.base)
        setup_code = """
from sf_veritas.custom_output_wrapper import get_custom_output_wrapper_django

get_custom_output_wrapper_django()
"""

        with open(base_path, "r+") as f:
            content = f.read()
            if "get_custom_output_wrapper_django()" not in content:
                f.write("\n" + setup_code)
                if PRINT_CONFIGURATION_STATUSES:
                    print("Custom output wrapper injected into Django.", log=False)
    except ModuleNotFoundError:
        if PRINT_CONFIGURATION_STATUSES:
            print(
                "Django not found; skipping output-wrapper injection",
                log=False,
            )
    except PermissionError:
        if PRINT_CONFIGURATION_STATUSES:
            print(
                "Permission error injecting output wrapper; skipping",
                log=False,
            )
    if PRINT_CONFIGURATION_STATUSES:
        print("find_and_modify_output_wrapper...DONE", log=False)


class SailfishMiddleware(MiddlewareMixin):
    """
    • process_request   – capture inbound SAILFISH_TRACING_HEADER header.
    • process_view      – emit one NetworkHop per view (skip Strawberry).
    • __call__ override – last-chance catcher for uncaught exceptions.
    • got_request_exception signal – main hook for 500-level errors.
    • process_exception – fallback for view-raised exceptions.
    """

    # ------------------------------------------------------------------ #
    # 0 | Signal registration (called once at server start-up)
    # ------------------------------------------------------------------ #
    def __init__(self, get_response):
        super().__init__(get_response)

        # Attach to Django's global exception signal so we ALWAYS
        # see real exceptions that become HTTP-500 responses.
        from django.core.signals import got_request_exception

        got_request_exception.disconnect(  # avoid dupes on reload
            self._on_exception_signal, dispatch_uid="sf_veritas_signal"
        )
        got_request_exception.connect(
            self._on_exception_signal,
            weak=False,
            dispatch_uid="sf_veritas_signal",
        )

    # ------------------------------------------------------------------ #
    # 1 | Signal handler  ← FIXED
    # ------------------------------------------------------------------ #
    def _on_exception_signal(self, sender, request, **kwargs):
        """
        Handle django.core.signals.got_request_exception.

        The signal doesn't pass the exception object; per Django's own
        implementation (and Sentry's approach) we fetch it from
        sys.exc_info().
        """
        import sys

        exc_type, exc_value, exc_tb = sys.exc_info()

        if SF_DEBUG:
            print(
                f"[[SailfishMiddleware._on_exception_signal]] "
                f"exc_value={exc_value!r}",
                log=False,
            )

        if exc_value:
            custom_excepthook(exc_type, exc_value, exc_tb)

    # ------------------------------------------------------------------ #
    # 2 | Last-chance wrapper (rarely triggered in WSGI but free)
    # ------------------------------------------------------------------ #
    def __call__(self, request):
        try:
            return super().__call__(request)
        except Exception as exc:
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise  # preserve default Django 500

    # ------------------------------------------------------------------ #
    # 3 | Header capture
    # ------------------------------------------------------------------ #
    def process_request(self, request):
        header_key = f"HTTP_{SAILFISH_TRACING_HEADER.upper().replace('-', '_')}"
        inbound = request.META.get(header_key)
        get_or_set_sf_trace_id(inbound, is_associated_with_inbound_request=True)
        if SF_DEBUG:
            print(
                f"[[SailfishMiddleware.process_request]] "
                f"key={header_key}, inbound={inbound}",
                log=False,
            )

    # ------------------------------------------------------------------ #
    # 4 | Network-hop emission  (unchanged)
    # ------------------------------------------------------------------ #
    def process_view(self, request, view_func, view_args, view_kwargs):
        module = getattr(view_func, "__module__", "")
        if module.startswith("strawberry"):
            return None

        code = getattr(view_func, "__code__", None)
        if not code:
            return None

        fname, lno = code.co_filename, code.co_firstlineno
        hop_key = (fname, lno)

        sent = getattr(request, "_sf_hops_sent", set())
        if hop_key not in sent:
            _, session_id = get_or_set_sf_trace_id()
            NetworkHopsTransmitter().send(
                session_id=session_id,
                line=str(lno),
                column="0",
                name=view_func.__name__,
                entrypoint=fname,
            )
            sent.add(hop_key)
            setattr(request, "_sf_hops_sent", sent)

    # ------------------------------------------------------------------ #
    # 5 | View-level exception hook (unchanged)
    # ------------------------------------------------------------------ #
    def process_exception(self, request, exception):
        print("[[SailfishMiddleware.process_exception]]", log=False)
        custom_excepthook(type(exception), exception, exception.__traceback__)


# --------------------------------------------------------------------------- #
# Helper – patch django.core.wsgi.get_wsgi_application once
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# Helper – patch django.core.wsgi.get_wsgi_application once
# --------------------------------------------------------------------------- #
def _patch_get_wsgi_application() -> None:
    """
    Replace ``django.core.wsgi.get_wsgi_application`` with a wrapper that:

    1. Runs ``django.setup()`` (as the original does),
    2. **Then** injects ``SailfishMiddleware`` into *settings.MIDDLEWARE*
       *after* settings are configured but *before* the first ``WSGIHandler``
       is built,
    3. Wraps the returned handler in our ``CustomExceptionMiddleware`` so we
       still have a last-chance catcher outside Django's stack.

    This mirrors the flow used by Sentry's Django integration.
    """
    try:
        from django.core import wsgi as _wsgi_mod
    except ImportError:  # pragma: no cover
        return

    if getattr(_wsgi_mod, "_sf_patched", False):
        return  # idempotent

    _orig_get_wsgi = _wsgi_mod.get_wsgi_application
    _MW_PATH = "sf_veritas.patches.web_frameworks.django.SailfishMiddleware"

    def _sf_get_wsgi_application(*args, **kwargs):
        # --- Step 1: exactly replicate original behaviour -----------------
        import django

        django.setup(set_prefix=False)  # configures settings & apps

        # --- Step 2: inject middleware *now* (settings are configured) ----
        from django.conf import settings

        if (
            hasattr(settings, "MIDDLEWARE")
            and isinstance(settings.MIDDLEWARE, list)
            and _MW_PATH not in settings.MIDDLEWARE
        ):
            settings.MIDDLEWARE.insert(0, _MW_PATH)

        # --- Step 3: build handler and wrap for last-chance exceptions ----
        from django.core.handlers.wsgi import WSGIHandler
        from sf_veritas.patches.web_frameworks.django import CustomExceptionMiddleware

        handler = WSGIHandler()
        return CustomExceptionMiddleware(handler)

    _wsgi_mod.get_wsgi_application = _sf_get_wsgi_application
    _wsgi_mod._sf_patched = True


def patch_django_middleware() -> None:
    """
    Public entry-point called by ``setup_interceptors``.

    • Inserts ``SailfishMiddleware`` for *already-configured* settings
      (run-server or ASGI).
    • Patches ``get_wsgi_application`` so *future* WSGI handlers created
      by third-party code inherit the middleware without relying on a
      configured settings object at import time.
    """

    try:
        from django.conf import settings
        from django.core.exceptions import ImproperlyConfigured
    except ImportError:  # Django not installed
        return

    _MW_PATH = "sf_veritas.patches.web_frameworks.django.SailfishMiddleware"

    # ---------- If settings are *already* configured, patch immediately ---
    try:
        if settings.configured and isinstance(
            getattr(settings, "MIDDLEWARE", None), list
        ):
            if _MW_PATH not in settings.MIDDLEWARE:
                settings.MIDDLEWARE.insert(0, _MW_PATH)
    except ImproperlyConfigured:
        # Settings not yet configured – safe to ignore; the WSGI patch below
        # will handle insertion once ``django.setup()`` runs.
        pass

    # ---------- Always patch get_wsgi_application (idempotent) ------------
    _patch_get_wsgi_application()

    if SF_DEBUG:
        print(
            "[[patch_django_middleware]] Sailfish Django integration ready", log=False
        )


class CustomExceptionMiddleware:
    """
    A universal last-chance exception wrapper that works for either
    • ASGI call signature:   (scope, receive, send)  → coroutine
    • WSGI call signature:   (environ, start_response) → iterable
    Every un-handled exception is funneled through ``custom_excepthook`` once.
    """

    def __init__(self, app):
        self.app = app

    # ------------------------------------------------------------------ #
    # Dispatcher – routes ASGI vs WSGI based on arity / argument shape
    # ------------------------------------------------------------------ #
    def __call__(self, *args, **kwargs):
        if len(args) == 3:
            # Heuristic: (scope, receive, send) for ASGI
            return self._asgi_call(*args)  # returns coroutine
        # Else assume classic WSGI: (environ, start_response)
        return self._wsgi_call(*args)  # returns iterable

    # ------------------------------------------------------------------ #
    # ASGI branch
    # ------------------------------------------------------------------ #
    async def _asgi_call(self, scope, receive, send):
        try:
            await self.app(scope, receive, send)
        except Exception as exc:  # noqa: BLE001
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise

    # ------------------------------------------------------------------ #
    # WSGI branch
    # ------------------------------------------------------------------ #
    def _wsgi_call(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        except Exception as exc:  # noqa: BLE001
            custom_excepthook(type(exc), exc, exc.__traceback__)
            raise

    # ------------------------------------------------------------------ #
    # Delegate attribute access so the wrapped app still behaves normally
    # ------------------------------------------------------------------ #
    def __getattr__(self, attr):
        return getattr(self.app, attr)
