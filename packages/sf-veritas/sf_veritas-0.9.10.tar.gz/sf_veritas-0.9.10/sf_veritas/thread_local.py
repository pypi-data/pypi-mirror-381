import builtins
import threading
import uuid
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any, Dict, Optional, Set, Tuple, Union
from uuid import UUID

from . import app_config
from .constants import NONSESSION_APPLOGS
from .env_vars import SF_DEBUG

# Define context variables
# You CANNOT switch this for another type - this is the ONLY version that works as of October 2024.
# Thread variables do not work, nor do globals.
# See https://elshad-karimov.medium.com/pythons-contextvars-the-most-powerful-feature-you-ve-never-heard-of-d636f4d34030
trace_id_ctx = ContextVar("trace_id", default=None)
handled_exceptions_ctx = ContextVar("handled_exceptions", default=set())
reentrancy_guard_logging_active_ctx = ContextVar(
    "reentrancy_guard_logging_active", default=False
)
reentrancy_guard_logging_preactive_ctx = ContextVar(
    "reentrancy_guard_logging_preactive", default=False
)
reentrancy_guard_print_active_ctx = ContextVar(
    "reentrancy_guard_print_active", default=False
)
reentrancy_guard_print_preactive_ctx = ContextVar(
    "reentrancy_guard_print_preactive", default=False
)
reentrancy_guard_exception_active_ctx = ContextVar(
    "reentrancy_guard_exception_active", default=False
)
reentrancy_guard_exception_preactive_ctx = ContextVar(
    "reentrancy_guard_exception_preactive", default=False
)
suppress_network_recording_ctx = ContextVar("suppress_network_recording", default=False)
reentrancy_guard_sys_stdout_active_ctx = ContextVar(
    "reentrancy_guard_sys_stdout_active", default=False
)

# Thread-local storage as a fallback
_thread_locals = threading.local()

_shared_trace_registry = {}
_shared_trace_registry_lock = threading.RLock()


def _set_shared_trace_id(trace_id: str) -> None:
    with _shared_trace_registry_lock:
        _shared_trace_registry["trace_id"] = trace_id


def _get_shared_trace_id() -> Optional[str]:
    with _shared_trace_registry_lock:
        return _shared_trace_registry.get("trace_id")


# Generalized get, set, and get_or_set functions for all properties
def _get_context_or_thread_local(
    ctx_var: ContextVar, attr_name: str, default: Any
) -> Any:
    return ctx_var.get() or getattr(_thread_locals, attr_name, default)


def _set_context_and_thread_local(
    ctx_var: ContextVar, attr_name: str, value: Any
) -> Any:
    ctx_var.set(value)
    setattr(_thread_locals, attr_name, value)
    return value


def unset_sf_trace_id() -> None:
    """
    Fully unsets the Sailfish trace ID from contextvars, thread-local storage,
    and the shared trace registry.
    """
    _set_shared_trace_id(None)
    _set_context_and_thread_local(trace_id_ctx, "trace_id", None)
    if SF_DEBUG:
        print("[[DEBUG]] unset_sf_trace_id: trace_id cleared", log=False)


def _get_or_set_context_and_thread_local(
    ctx_var: ContextVar, attr_name: str, value_if_not_set
) -> Tuple[bool, Any]:
    value = ctx_var.get() or getattr(_thread_locals, attr_name, None)
    if value is None:
        return _set_context_and_thread_local(ctx_var, attr_name, value_if_not_set)
    return value


# Trace ID functions
def get_sf_trace_id() -> Optional[Union[str, UUID]]:
    shared_trace_id = _get_shared_trace_id()
    if shared_trace_id:
        return shared_trace_id
    return _get_context_or_thread_local(trace_id_ctx, "trace_id", None)


def set_sf_trace_id(trace_id: Union[str, UUID]) -> Union[str, UUID]:
    _set_shared_trace_id(str(trace_id))
    return _set_context_and_thread_local(trace_id_ctx, "trace_id", trace_id)


def get_or_set_sf_trace_id(
    new_trace_id_if_not_set: Optional[str] = None,
    is_associated_with_inbound_request: bool = False,
) -> Tuple[bool, Union[str, UUID]]:
    if new_trace_id_if_not_set:
        if SF_DEBUG:
            print(
                f"[trace_id] Setting new trace_id from argument: {new_trace_id_if_not_set}",
                log=False,
            )
        set_sf_trace_id(new_trace_id_if_not_set)
        return True, new_trace_id_if_not_set

    trace_id = get_sf_trace_id()
    if trace_id:
        if SF_DEBUG:
            print(f"[trace_id] Returning existing trace_id: {trace_id}", log=False)
        return False, trace_id

    if SF_DEBUG:
        print("[trace_id] No trace_id found. Generating new trace_id.", log=False)
    unique_id = uuid.uuid4()
    trace_id = f"{NONSESSION_APPLOGS}-v3/{app_config._sailfish_api_key}/{unique_id}"
    set_sf_trace_id(trace_id)
    if SF_DEBUG:
        print(f"[trace_id] Generated and set new trace_id: {trace_id}", log=False)
    return True, trace_id


# Handled exceptions functions
def get_handled_exceptions() -> Set[Any]:
    return _get_context_or_thread_local(
        handled_exceptions_ctx, "handled_exceptions", set()
    )


def set_handled_exceptions(exceptions_set: Set[Any]) -> Set[Any]:
    return _set_context_and_thread_local(
        handled_exceptions_ctx, "handled_exceptions", exceptions_set
    )


def get_or_set_handled_exceptions(default: set = None) -> Tuple[bool, Set[Any]]:
    if default is None:
        default = set()
    return _get_or_set_context_and_thread_local(
        handled_exceptions_ctx, "handled_exceptions", default
    )


def mark_exception_handled(exception) -> None:
    """
    Marks an exception as handled to avoid duplicate processing.
    """
    handled_exceptions = get_handled_exceptions()
    handled_exceptions.add(id(exception))
    set_handled_exceptions(handled_exceptions)

    # Set the `_handled` attribute on the exception if it exists
    if hasattr(exception, "_handled"):
        setattr(exception, "_handled", True)


def has_handled_exception(exception) -> bool:
    """
    Checks if an exception has been handled.
    """
    # Check both thread-local context and the `_handled` attribute
    return id(exception) in get_handled_exceptions() or getattr(
        exception, "_handled", False
    )


def reset_handled_exceptions() -> Set[Any]:
    return set_handled_exceptions(set())


# Reentrancy guards functions (logging)
def get_reentrancy_guard_logging_active() -> bool:
    return _get_context_or_thread_local(
        reentrancy_guard_logging_active_ctx, "reentrancy_guard_logging_active", False
    )


def set_reentrancy_guard_logging_active(value: bool) -> bool:
    return _set_context_and_thread_local(
        reentrancy_guard_logging_active_ctx, "reentrancy_guard_logging_active", value
    )


def get_or_set_reentrancy_guard_logging_active(
    value_if_not_set: bool,
) -> Tuple[bool, bool]:
    return _get_or_set_context_and_thread_local(
        reentrancy_guard_logging_active_ctx,
        "reentrancy_guard_logging_active",
        value_if_not_set,
    )


def activate_reentrancy_guards_logging() -> bool:
    set_reentrancy_guard_logging_active(True)
    set_reentrancy_guard_logging_preactive(True)
    return True


def get_reentrancy_guard_logging_preactive() -> bool:
    return _get_context_or_thread_local(
        reentrancy_guard_logging_preactive_ctx,
        "reentrancy_guard_logging_preactive",
        False,
    )


def set_reentrancy_guard_logging_preactive(value: bool) -> bool:
    return _set_context_and_thread_local(
        reentrancy_guard_logging_preactive_ctx,
        "reentrancy_guard_logging_preactive",
        value,
    )


def get_or_set_reentrancy_guard_logging_preactive(
    value_if_not_set: bool,
) -> Tuple[bool, bool]:
    return _get_or_set_context_and_thread_local(
        reentrancy_guard_logging_preactive_ctx,
        "reentrancy_guard_logging_preactive",
        value_if_not_set,
    )


def activate_reentrancy_guards_logging_preactive() -> bool:
    return set_reentrancy_guard_logging_preactive(True)


# Reentrancy guards functions (stdout)
def get_reentrancy_guard_sys_stdout_active() -> bool:
    return _get_context_or_thread_local(
        reentrancy_guard_sys_stdout_active_ctx,
        "reentrancy_guard_sys_stdout_active",
        False,
    )


def set_reentrancy_guard_sys_stdout_active(value: bool) -> bool:
    return _set_context_and_thread_local(
        reentrancy_guard_sys_stdout_active_ctx,
        "reentrancy_guard_sys_stdout_active",
        value,
    )


def activate_reentrancy_guards_sys_stdout() -> bool:
    set_reentrancy_guard_sys_stdout_active(True)
    return True


# Reentrancy guards functions (print)
def get_reentrancy_guard_print_active() -> bool:
    return _get_context_or_thread_local(
        reentrancy_guard_print_active_ctx, "reentrancy_guard_print_active", False
    )


def set_reentrancy_guard_print_active(value: bool) -> bool:
    return _set_context_and_thread_local(
        reentrancy_guard_print_active_ctx, "reentrancy_guard_print_active", value
    )


def get_or_set_reentrancy_guard_print_active(
    value_if_not_set: bool,
) -> Tuple[bool, bool]:
    return _get_or_set_context_and_thread_local(
        reentrancy_guard_print_active_ctx,
        "reentrancy_guard_print_active",
        value_if_not_set,
    )


def activate_reentrancy_guards_print() -> bool:
    set_reentrancy_guard_print_active(True)
    set_reentrancy_guard_print_preactive(True)
    return True


def get_reentrancy_guard_print_preactive() -> bool:
    return _get_context_or_thread_local(
        reentrancy_guard_print_preactive_ctx, "reentrancy_guard_print_preactive", False
    )


def set_reentrancy_guard_print_preactive(value: bool) -> bool:
    return _set_context_and_thread_local(
        reentrancy_guard_print_preactive_ctx, "reentrancy_guard_print_preactive", value
    )


def get_or_set_reentrancy_guard_print_preactive(
    value_if_not_set: bool,
) -> Tuple[bool, bool]:
    return _get_or_set_context_and_thread_local(
        reentrancy_guard_print_preactive_ctx,
        "reentrancy_guard_print_preactive",
        value_if_not_set,
    )


def activate_reentrancy_guards_print_preactive() -> bool:
    return set_reentrancy_guard_print_preactive(True)


# Reentrancy guards functions (exception)
def get_reentrancy_guard_exception_active() -> bool:
    return _get_context_or_thread_local(
        reentrancy_guard_exception_active_ctx,
        "reentrancy_guard_exception_active",
        False,
    )


def set_reentrancy_guard_exception_active(value: bool) -> bool:
    return _set_context_and_thread_local(
        reentrancy_guard_exception_active_ctx,
        "reentrancy_guard_exception_active",
        value,
    )


def get_or_set_reentrancy_guard_exception_active(
    value_if_not_set: bool,
) -> Tuple[bool, bool]:
    return _get_or_set_context_and_thread_local(
        reentrancy_guard_exception_active_ctx,
        "reentrancy_guard_exception_active",
        value_if_not_set,
    )


def activate_reentrancy_guards_exception() -> bool:
    set_reentrancy_guard_exception_active(True)
    set_reentrancy_guard_exception_preactive(True)
    return True


def get_reentrancy_guard_exception_preactive() -> bool:
    return _get_context_or_thread_local(
        reentrancy_guard_exception_preactive_ctx,
        "reentrancy_guard_exception_preactive",
        False,
    )


def set_reentrancy_guard_exception_preactive(value: bool) -> bool:
    return _set_context_and_thread_local(
        reentrancy_guard_exception_preactive_ctx,
        "reentrancy_guard_exception_preactive",
        value,
    )


def get_or_set_reentrancy_guard_exception_preactive(
    value_if_not_set: bool,
) -> Tuple[bool, bool]:
    return _get_or_set_context_and_thread_local(
        reentrancy_guard_exception_preactive_ctx,
        "reentrancy_guard_exception_preactive",
        value_if_not_set,
    )


def activate_reentrancy_guards_exception_preactive() -> bool:
    return set_reentrancy_guard_exception_preactive(True)


# Get and set context
def get_context() -> Dict[str, Any]:
    """Get the current context values for all properties."""
    return {
        "trace_id": get_sf_trace_id(),
        "handled_exceptions": get_handled_exceptions(),
        "reentrancy_guard_logging_active": get_reentrancy_guard_logging_active(),
        "reentrancy_guard_logging_preactive": get_reentrancy_guard_logging_preactive(),
        "reentrancy_guard_print_active": get_reentrancy_guard_print_active(),
        "reentrancy_guard_print_preactive": get_reentrancy_guard_print_preactive(),
        "reentrancy_guard_exception_active": get_reentrancy_guard_exception_active(),
        "reentrancy_guard_exception_preactive": get_reentrancy_guard_exception_preactive(),
        "reentrancy_guard_sys_stdout_active": get_reentrancy_guard_sys_stdout_active(),
    }


def set_context(context) -> None:
    """Set the current context values for all properties."""
    set_sf_trace_id(context.get("trace_id"))
    set_handled_exceptions(context.get("handled_exceptions", set()))
    set_reentrancy_guard_logging_active(
        context.get("reentrancy_guard_logging_active", False)
    )
    set_reentrancy_guard_logging_preactive(
        context.get("reentrancy_guard_logging_preactive", False)
    )
    set_reentrancy_guard_print_active(
        context.get("reentrancy_guard_print_active", False)
    )
    set_reentrancy_guard_print_preactive(
        context.get("reentrancy_guard_print_preactive", False)
    )
    set_reentrancy_guard_exception_active(
        context.get("reentrancy_guard_exception_active", False)
    )
    set_reentrancy_guard_exception_preactive(
        context.get("reentrancy_guard_exception_preactive", False)
    )
    set_reentrancy_guard_sys_stdout_active(
        context.get("reentrancy_guard_sys_stdout_active", False)
    )


@contextmanager
def suppress_network_recording():
    token = suppress_network_recording_ctx.set(True)
    try:
        yield
    finally:
        suppress_network_recording_ctx.reset(token)


def is_network_recording_suppressed() -> bool:
    return suppress_network_recording_ctx.get()
