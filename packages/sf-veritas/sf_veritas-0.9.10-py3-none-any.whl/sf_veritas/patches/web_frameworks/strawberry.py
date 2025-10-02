import inspect
import logging
import sys
from importlib.util import find_spec
from typing import Any, Callable, Set, Tuple

from ...custom_excepthook import custom_excepthook
from ...env_vars import PRINT_CONFIGURATION_STATUSES, SF_DEBUG
from ...regular_data_transmitter import NetworkHopsTransmitter
from ...thread_local import get_or_set_sf_trace_id
from .utils import _is_user_code, _unwrap_user_func

logger = logging.getLogger(__name__)

# Track if Strawberry has already been patched to prevent multiple patches
_is_strawberry_patched = False


def get_extension():
    from strawberry.extensions import SchemaExtension

    class CustomErrorHandlingExtension(SchemaExtension):
        def __init__(self, *, execution_context):
            self.execution_context = execution_context

        def on_request_start(self):
            if SF_DEBUG:
                print("Starting GraphQL request", log=False)

        def on_request_end(self):
            if SF_DEBUG:
                print("Ending GraphQL request", log=False)
            if not self.execution_context.errors:
                return
            for error in self.execution_context.errors:
                if SF_DEBUG:
                    print(f"Handling GraphQL error: {error}", log=False)
                custom_excepthook(type(error), error, error.__traceback__)

        def on_validation_start(self):
            if SF_DEBUG:
                print("Starting validation of GraphQL request", log=False)

        def on_validation_end(self):
            if SF_DEBUG:
                print("Ending validation of GraphQL request", log=False)

        def on_execution_start(self):
            if SF_DEBUG:
                print("Starting execution of GraphQL request", log=False)

        def on_resolver_start(self, resolver, obj, info, **kwargs):
            if SF_DEBUG:
                print(f"Starting resolver {resolver.__name__}", log=False)

        def on_resolver_end(self, resolver, obj, info, **kwargs):
            if SF_DEBUG:
                print(f"Ending resolver {resolver.__name__}", log=False)

        def on_error(self, error: Exception):
            if SF_DEBUG:
                print(f"Handling error in resolver: {error}", log=False)
            custom_excepthook(type(error), error, error.__traceback__)

    return CustomErrorHandlingExtension


def get_network_hop_extension() -> "type[SchemaExtension]":
    """
    Strawberry SchemaExtension that emits a collectNetworkHops mutation for the
    *first* user-land frame executed inside every resolver (sync or async).
    """

    from strawberry.extensions import SchemaExtension

    # --------------------------------------------------------------------- #
    # Helper predicates
    # --------------------------------------------------------------------- #
    # Extended dig:  __wrapped__, closure cells *and* common attribute names
    # --------------------------------------------------------------------- #
    # Extension class
    # --------------------------------------------------------------------- #
    class NetworkHopExtension(SchemaExtension):
        supports_sync = supports_async = True
        _sent: Set[Tuple[str, int]] = set()  # class-level: de-dupe per request

        # ---------------- internal emit helper ---------------- #
        @staticmethod
        def _emit(frame, info):
            filename, line_no, func_name = (
                frame.f_code.co_filename,
                frame.f_lineno,
                frame.f_code.co_name,
            )
            if (filename, line_no) in NetworkHopExtension._sent:
                return
            _, session_id = get_or_set_sf_trace_id()
            if SF_DEBUG:
                print(
                    f"[[NetworkHopExtension]] SEND → {func_name} "
                    f"({filename}:{line_no}) session={session_id}",
                    log=False,
                )
            NetworkHopsTransmitter().send(
                session_id=session_id,
                line=str(line_no),
                column="0",
                name=func_name,
                entrypoint=filename,
            )

        # ---------------- tracer factory ---------------- #
        def _make_tracer(self, info):
            def tracer(frame, event, arg):
                if event.startswith("c_"):
                    return
                if event == "call":
                    if _is_user_code(frame.f_code.co_filename):

                        self._emit(frame, info)
                        sys.setprofile(None)
                        return
                    return tracer  # keep tracing until we hit user code

            return tracer

        # ---------------- wrappers ---------------- #
        def resolve(self, _next, root, info, *args, **kwargs):
            user_fn = _unwrap_user_func(_next)
            tracer = self._make_tracer(info)
            sys.setprofile(tracer)
            try:
                return _next(root, info, *args, **kwargs)
            finally:
                sys.setprofile(None)  # safety-net

        async def resolve_async(self, _next, root, info, *args, **kwargs):
            user_fn = _unwrap_user_func(_next)
            tracer = self._make_tracer(info)
            sys.setprofile(tracer)
            try:
                return await _next(root, info, *args, **kwargs)
            finally:
                sys.setprofile(None)

    return NetworkHopExtension


def patch_strawberry_module(strawberry):
    """Patch Strawberry to ensure exceptions go through the custom excepthook."""
    global _is_strawberry_patched
    if _is_strawberry_patched:
        if SF_DEBUG:
            print(
                "[[DEBUG]] Strawberry has already been patched, skipping. [[/DEBUG]]",
                log=False,
            )
        return

    try:
        # Backup the original execute method from Strawberry
        original_execute = strawberry.execution.execute.execute

        async def custom_execute(*args, **kwargs):
            try:
                if SF_DEBUG:
                    print(
                        "[[DEBUG]] Executing patched Strawberry execute function. [[/DEBUG]]",
                        log=False,
                    )
                return await original_execute(*args, **kwargs)
            except Exception as e:
                if SF_DEBUG:
                    print(
                        "[[DEBUG]] Intercepted exception in Strawberry execute. [[/DEBUG]]",
                        log=False,
                    )
                # Invoke custom excepthook globally
                sys.excepthook(type(e), e, e.__traceback__)
                raise

        # Replace Strawberry's execute function with the patched version
        strawberry.execution.execute.execute = custom_execute
        _is_strawberry_patched = True
        if SF_DEBUG:
            print(
                "[[DEBUG]] Successfully patched Strawberry execute function. [[/DEBUG]]",
                log=False,
            )
    except Exception as error:
        if SF_DEBUG:
            print(
                f"[[DEBUG]] Failed to patch Strawberry: {error}. [[/DEBUG]]", log=False
            )


class CustomImportHook:
    """Import hook to intercept the import of 'strawberry' modules."""

    def find_spec(self, fullname, path, target=None):
        global _is_strawberry_patched
        if fullname == "strawberry" and not _is_strawberry_patched:
            if SF_DEBUG:
                print(
                    f"[[DEBUG]] Intercepting import of {fullname}. [[/DEBUG]]",
                    log=False,
                )
            return find_spec(fullname)
        if fullname.startswith("strawberry_django"):
            return None  # Let default import handle strawberry_django

    def exec_module(self, module):
        if SF_DEBUG:
            print(
                f"[[DEBUG]] Executing module: {module.__name__}. [[/DEBUG]]", log=False
            )
        # Execute the module normally
        module_spec = module.__spec__
        if module_spec and module_spec.loader:
            module_spec.loader.exec_module(module)
        # Once strawberry is loaded, patch it
        if module.__name__ == "strawberry" and not _is_strawberry_patched:
            patch_strawberry_module(module)


def patch_strawberry_schema():
    """Patch strawberry.Schema to include both Sailfish and NetworkHop extensions by default."""
    try:
        import strawberry

        original_schema_init = strawberry.Schema.__init__

        def patched_schema_init(self, *args, extensions=None, **kwargs):
            if extensions is None:
                extensions = []

            # Add the custom error handling extension
            sailfish_ext = get_extension()
            if sailfish_ext not in extensions:
                extensions.append(sailfish_ext)

            # Add the network hop extension
            hop_ext = get_network_hop_extension()
            if hop_ext not in extensions:
                extensions.append(hop_ext)

            # Call the original constructor
            original_schema_init(self, *args, extensions=extensions, **kwargs)

            if SF_DEBUG:
                print(
                    "[[DEBUG]] Patched strawberry.Schema to include Sailfish & NetworkHop extensions. [[/DEBUG]]",
                    log=False,
                )

        # Apply the patch
        strawberry.Schema.__init__ = patched_schema_init

        if SF_DEBUG:
            print(
                "[[DEBUG]] Successfully patched strawberry.Schema. [[/DEBUG]]",
                log=False,
            )
    except ImportError:
        if SF_DEBUG:
            print(
                "[[DEBUG]] Strawberry is not installed. Skipping schema patching. [[/DEBUG]]",
                log=False,
            )
