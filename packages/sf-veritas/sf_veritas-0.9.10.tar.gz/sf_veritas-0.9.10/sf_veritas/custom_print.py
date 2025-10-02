import builtins
import sys

from .env_vars import SF_DEBUG
from .thread_local import (
    _thread_locals,
    activate_reentrancy_guards_sys_stdout,
    get_or_set_sf_trace_id,
)


def custom_print(*args, log=True, **kwargs):
    """
    Custom print function to intercept print statements.
    """
    # Prepare the message to print
    print_args = ("[[CUSTOM-PRINT]]", *args, "[[/CUSTOM-PRINT]]") if SF_DEBUG else args
    activate_reentrancy_guards_sys_stdout()
    builtins._original_print(  # pylint: disable=protected-access; This is added by our interceptor
        *print_args, file=sys.__stdout__, **kwargs
    )

    message = " ".join(map(str, args))
    # If log is True, send the message to the logging system
    if log and message.strip():
        _, trace_id = get_or_set_sf_trace_id()
        if SF_DEBUG:
            print(
                "UnifiedInterceptor.custom_print...SENDING DATA...args=",
                (message, trace_id),
                trace_id,
                log=False,
            )
        sys.stdout.print_interceptor.do_send((message, trace_id), trace_id)
