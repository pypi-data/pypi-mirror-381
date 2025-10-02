import atexit
import builtins
import functools
import inspect
import logging
import os
import re
import sys
import threading
from types import ModuleType
from typing import Dict, List, Optional, Union

from pydantic import validate_call

from . import app_config
from .custom_excepthook import (
    custom_excepthook,
    custom_thread_excepthook,
    start_profiling,
)
from .custom_log_handler import CustomLogHandler
from .env_vars import LOG_LEVEL, PRINT_CONFIGURATION_STATUSES, SF_DEBUG
from .exception_metaclass import PatchedException
from .interceptors import PrintInterceptor
from .patches.network_libraries import patch_all_http_clients
from .patches.web_frameworks import patch_web_frameworks
from .shutdown_flag import set_shutdown_flag
from .thread_local import (
    _thread_locals,
    activate_reentrancy_guards_sys_stdout,
    get_or_set_sf_trace_id,
    get_reentrancy_guard_sys_stdout_active,
)
from .local_env_detect import set_sf_is_local_flag
from .timeutil import TimeSync

# from .patches.django import find_and_modify_output_wrapper

STRINGS_NOT_FOUND_IN_CALLER_LOCATIONS = {
    "site-packages",
    "dist-packages",
    "venv",
    "/lib/python",
    "\\lib\\python",
    "sf-veritas",
}


class UnifiedInterceptor:
    def __init__(self):
        self.log_interceptor = CustomLogHandler()
        self.print_interceptor = PrintInterceptor()
        self._original_stdout = sys.stdout  # Store the original sys.stdout
        self._original_stderr = sys.stderr  # Store the original sys.stderr
        self._lock = threading.Lock()

    def write(self, message):
        """
        Custom write method for intercepting sys.stdout.write calls.
        """
        if get_reentrancy_guard_sys_stdout_active() or (
            hasattr(_thread_locals, "reentrancy_guard_logging_active")
            and _thread_locals.reentrancy_guard_logging_active
        ):
            self._original_stdout.write(message)
            self._original_stdout.flush()
            return

        _, trace_id = get_or_set_sf_trace_id()
        with self._lock:
            # Always write to the original stdout
            self._original_stdout.write(message)
            self._original_stdout.flush()

            if message.strip():
                if SF_DEBUG:
                    # Bypass our custom print/interceptor entirely:
                    self._original_stdout.write(
                        f"UnifiedInterceptor.write...SENDING DATA...args={(message, trace_id)}\n"
                    )
                    self._original_stdout.flush()
                self.print_interceptor.do_send((message, trace_id), trace_id)

    def flush(self):
        """
        Custom flush method for sys.stdout.
        """
        self._original_stdout.flush()

    def create_custom_print(self):
        """
        Create a custom print function that includes `log` as a keyword argument.
        """

        def custom_print(*args, log=True, **kwargs):
            """
            Custom print function to intercept print statements.
            """
            # Prepare the message to print
            print_args = (
                (f"[[CUSTOM-PRINT; log={log}]]", *args, "[[/CUSTOM-PRINT]]")
                if SF_DEBUG
                else args
            )
            modified_message = " ".join(map(str, print_args))

            # Output the message to the original stdout
            activate_reentrancy_guards_sys_stdout()
            self._original_stdout.write(modified_message + "\n")
            self._original_stdout.flush()

            message = " ".join(map(str, args))
            # If log is True, send the message to the logging system
            if log and message.strip():
                _, trace_id = get_or_set_sf_trace_id()
                if SF_DEBUG:
                    # Bypass the interceptor here as well
                    self._original_stdout.write(
                        f"UnifiedInterceptor.custom_print...SENDING DATA...args={(message, trace_id)}\n"
                    )
                    self._original_stdout.flush()
                self.print_interceptor.do_send((message, trace_id), trace_id)
                # threading.Thread(
                #     target=self.print_interceptor.send, args=(message, trace_id)
                # ).start()

        return custom_print

    def __getattr__(self, attr):
        """
        Delegate attribute access to the original stdout or stderr.
        """
        if hasattr(self._original_stdout, attr):
            return getattr(self._original_stdout, attr)
        # TODO - Sibyl post-launch - handle stderr interception
        # elif hasattr(self._original_stderr, attr):
        #     return getattr(self._original_stderr, attr)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{attr}'"
            )

    def intercept_stdout(self):
        """
        Replace sys.stdout and builtins.print to intercept all output.
        """
        if PRINT_CONFIGURATION_STATUSES:
            self._original_stdout.write("Intercepting stdout and print...\n")
            self._original_stdout.flush()

        # Replace the stdout
        sys.stdout = self
        # TODO - Sibyl post-launch - handle stderr interception
        # sys.stderr = self

        # Create a custom print function with modified signature
        custom_print_function = self.create_custom_print()

        builtins.print = functools.partial(custom_print_function)

        # Check if __builtins__ is a module or a dictionary and override accordingly
        if isinstance(__builtins__, dict):
            __builtins__["print"] = custom_print_function
        elif isinstance(__builtins__, ModuleType):
            setattr(__builtins__, "print", custom_print_function)

        # Explicitly override the print function in the `__main__` module if present
        if "__main__" in sys.modules:
            sys.modules["__main__"].__dict__["print"] = custom_print_function

        # Ensure `print` is overridden in the `builtins` module reference
        sys.modules["builtins"].print = custom_print_function

        if PRINT_CONFIGURATION_STATUSES:
            self._original_stdout.write("Intercepting stdout and print...DONE\n")
            self._original_stdout.flush()

    def intercept_exceptions(self):
        """
        Intercept all uncaught exceptions globally and in threads.
        """
        start_profiling()

        if PRINT_CONFIGURATION_STATUSES:
            self._original_stdout.write("Intercepting uncaught exceptions...\n")
            self._original_stdout.flush()

        # Intercept uncaught exceptions globally
        sys.excepthook = custom_excepthook

        # If available, intercept uncaught exceptions in threads (Python 3.8+)
        if hasattr(threading, "excepthook"):
            threading.excepthook = custom_thread_excepthook

        if PRINT_CONFIGURATION_STATUSES:
            self._original_stdout.write("Intercepting uncaught exceptions...DONE\n")
            self._original_stdout.flush()

    # TODO - Figure out how to make this work universally
    def patch_exception_class(self):
        """
        Safely patch `builtins.Exception` with `PatchedException` while providing a fallback.
        """
        import builtins

        # Check if Exception has already been patched
        if hasattr(builtins.Exception, "transmit_to_sailfish"):
            return  # Already patched, no action needed

        try:

            if PRINT_CONFIGURATION_STATUSES:
                self._original_stdout.write("Monkey-patching Exceptions class...\n")
                self._original_stdout.flush()
            # Backup original Exception
            _ = builtins.Exception
            # Patch built-in Exception
            builtins.Exception = PatchedException
            if PRINT_CONFIGURATION_STATUSES:
                self._original_stdout.write("Monkey-patching Exceptions class...DONE\n")
                self._original_stdout.flush()
        except Exception as e:
            # Log or handle failure to patch
            print(f"[Warning] Failed to patch `builtins.Exception`: {e}")


@validate_call
def setup_interceptors(
    api_key: str,
    graphql_endpoint: str = None,
    service_identifier: Optional[str] = None,
    service_version: Optional[str] = None,
    git_sha: Optional[str] = None,
    service_additional_metadata: Optional[
        Dict[str, Union[str, int, float, None]]
    ] = None,
    profiling_mode_enabled: bool = False,  # Profiling mode argument to enable or disable profiling
    profiling_max_depth: int = 5,
    domains_to_not_propagate_headers_to: Optional[List[str]] = None,
    site_and_dist_packages_to_collect_local_variables_on: Optional[List[str]] = None,
    setup_global_time_at_app_spinup: bool = True,
):
    if service_identifier is None:
        service_identifier = os.getenv("SERVICE_VERSION", os.getenv("GIT_SHA"))
    if git_sha is None:
        git_sha = os.getenv("GIT_SHA")
    app_config._service_identifier = service_identifier
    app_config._service_version = service_version
    app_config._git_sha = git_sha
    app_config._service_additional_metadata = service_additional_metadata
    app_config._profiling_mode_enabled = profiling_mode_enabled
    app_config._profiling_max_depth = profiling_max_depth
    app_config._set_site_and_dist_packages_to_collect_local_variables_on = (
        site_and_dist_packages_to_collect_local_variables_on
    )

    # Caller location - navigate up the stack to see if the interceptor was set in code -vs- CLI usage
    for frame in inspect.stack():
        if any(
            [
                string_item in frame.filename
                for string_item in STRINGS_NOT_FOUND_IN_CALLER_LOCATIONS
            ]
        ):
            continue
        app_config._setup_interceptors_call_filename = frame.filename
        app_config._setup_interceptors_call_lineno = frame.lineno
        break

    # Use provided or default API Key and GraphQL endpoint
    app_config._sailfish_api_key = api_key
    app_config._sailfish_graphql_endpoint = (
        graphql_endpoint or app_config._sailfish_graphql_endpoint
    )

    # Check if the interceptors have already been initialized
    if app_config._interceptors_initialized:
        if SF_DEBUG:
            print("[[DEBUG]] Interceptors already set up. Skipping setup.", log=False)
        return  # Exit early to prevent duplicate setup

    if not app_config._sailfish_api_key:
        raise RuntimeError(
            "The 'api_key' parameter is missing. Please provide a valid value."
        )

    if PRINT_CONFIGURATION_STATUSES:
        print("Setting up interceptors")

    # Setup shutdown flag to prevent issues
    atexit.register(set_shutdown_flag)

    # Setup Global Time Sync
    if setup_global_time_at_app_spinup:
        TimeSync.get_instance()

    # Determine if instance is local or not
    set_sf_is_local_flag()
    # Setup UnifiedInterceptor
    unified_interceptor = UnifiedInterceptor()

    # Set up custom exception hook
    unified_interceptor.intercept_exceptions()

    # Set up logging
    logging.basicConfig(level=LOG_LEVEL)
    logger = logging.getLogger()
    logger.addHandler(CustomLogHandler())

    # Intercept stdout and print
    unified_interceptor.intercept_stdout()

    # Set up custom output wrappers
    patch_web_frameworks()

    # Patch requests and other core HTTP libraries
    patch_all_http_clients(domains_to_not_propagate_headers_to)

    # Mark interceptors as initialized to prevent re-running
    app_config._interceptors_initialized = True

    if PRINT_CONFIGURATION_STATUSES:
        print("Interceptors setup completed.", log=False)
