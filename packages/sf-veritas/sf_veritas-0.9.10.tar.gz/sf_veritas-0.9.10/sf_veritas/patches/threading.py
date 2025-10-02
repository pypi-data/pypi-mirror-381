import threading

from ..thread_local import get_context, set_context

_original_thread_init = threading.Thread.__init__


def patched_thread_init(self, *args, **kwargs):
    current_context = get_context()

    original_target = kwargs.get("target")
    if original_target:

        def wrapped_target(*targs, **tkwargs):
            set_context(current_context)
            original_target(*targs, **tkwargs)

        kwargs["target"] = wrapped_target
    elif args and callable(args[0]):
        original_target = args[0]

        def wrapped_target(*targs, **tkwargs):
            set_context(current_context)
            original_target(*targs, **tkwargs)

        args = (wrapped_target,) + args[1:]

    _original_thread_init(self, *args, **kwargs)


def patch_threading():
    threading.Thread.__init__ = patched_thread_init
