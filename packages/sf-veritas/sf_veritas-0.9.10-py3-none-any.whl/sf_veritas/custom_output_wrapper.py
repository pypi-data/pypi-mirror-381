import re
import sys
import threading

# from ._to_be_deleted__custom_output_wrapper_stderr import CustomOutputWrapperStdErr
from .env_vars import PRINT_CONFIGURATION_STATUSES, SF_DEBUG
from .interceptors import PrintInterceptor
from .thread_local import _thread_locals, get_or_set_sf_trace_id


class CustomOutputWrapper:
    def __init__(self, original):
        self.original = original
        self.print_interceptor = PrintInterceptor()
        self._lock = threading.Lock()

    def write(self, msg):
        if (
            hasattr(_thread_locals, "reentrancy_guard_logging_active")
            and _thread_locals.reentrancy_guard_logging_active
        ):
            self.original.write(msg)
            self.original.flush()
            return

        with self._lock:
            # Add custom tags if SF_DEBUG is enabled
            msg_with_tags = (
                f"[[CUSTOM-OUTPUT]] {msg} [[/CUSTOM-OUTPUT]]\n" if SF_DEBUG else msg
            )
            self.original.write(msg_with_tags)
            self.original.flush()

            # Intercept the message and log it
            # self.print_interceptor.send(msg_with_tags)
            pattern = r"HTTP\s(POST|GET)\s(\/healthz|\/graphql\/)\s.*"
            if re.match(pattern, msg):
                return

            _, trace_id = get_or_set_sf_trace_id()
            if SF_DEBUG:
                print(
                    "CustomOutputWrapper...SENDING DATA...args=",
                    (msg_with_tags, trace_id),
                    trace_id,
                    log=False,
                )
            self.print_interceptor.do_send((msg_with_tags, trace_id), trace_id)

    def __getattr__(self, attr):
        return getattr(self.original, attr)


def setup_custom_output_wrappers():
    if PRINT_CONFIGURATION_STATUSES:
        print("setup_custom_output_wrappers")
    sys.stdout = CustomOutputWrapper(sys.stdout)
    # sys.stderr = CustomOutputWrapperStdErr(sys.stderr)  # TODO - uncomment
    if PRINT_CONFIGURATION_STATUSES:
        print("setup_custom_output_wrappers...DONE")


def get_custom_output_wrapper_django():
    from django.core.management.base import OutputWrapper

    class CustomOutputWrapperDjango(OutputWrapper):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.print_interceptor = PrintInterceptor()

        def write(self, msg="", style_func=None, ending=None):
            if (
                hasattr(_thread_locals, "reentrancy_guard_logging_active")
                and _thread_locals.reentrancy_guard_logging_active
            ):
                super().write(msg, style_func, ending)
                return

            # Add custom tags if SF_DEBUG is enabled
            if style_func is None:
                style_func = lambda x: (
                    f"[[CUSTOM-OUTPUT-DJANGO]] {x} [[/CUSTOM-OUTPUT-DJANGO]]\n"
                    if SF_DEBUG
                    else x
                )

            # Use the original write method
            super().write(msg, style_func, ending)

            pattern = r"HTTP\s(POST|GET)\s(\/healthz|\/graphql\/)\s.*"
            if re.match(pattern, msg):
                return

            # Intercept the message and log it
            message = msg if ending is None else msg + ending

            _, trace_id = get_or_set_sf_trace_id()
            if SF_DEBUG:
                print(
                    "get_custom_output_wrapper_django...SENDING DATA...",
                    message,
                    trace_id,
                    log=False,
                )
            self.print_interceptor.do_send((message, trace_id), trace_id)

    return CustomOutputWrapperDjango
