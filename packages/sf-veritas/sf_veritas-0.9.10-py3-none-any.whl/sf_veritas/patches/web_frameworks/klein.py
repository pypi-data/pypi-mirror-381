import functools

from ...constants import SAILFISH_TRACING_HEADER
from ...thread_local import get_or_set_sf_trace_id


def patch_klein():
    """
    Monkey-patch Klein.route so that every @app.route endpoint first
    extracts SAILFISH_TRACING_HEADER and sets our ContextVar, then calls the user handler.
    No-op if Klein isn't installed.
    """
    try:
        import klein
    except ImportError:
        return

    original_route = klein.Klein.route

    def patched_route(self, *args, **kwargs):
        # Grab Klein's decorator for this pattern
        original_decorator = original_route(self, *args, **kwargs)

        def new_decorator(fn):
            @functools.wraps(fn)
            def wrapped(request, *f_args, **f_kwargs):
                header = request.getHeader(SAILFISH_TRACING_HEADER)
                if header:
                    get_or_set_sf_trace_id(
                        header, is_associated_with_inbound_request=True
                    )
                # Now that our ContextVar is set, call the real handler
                return fn(request, *f_args, **f_kwargs)

            # Register the wrapped handler instead of the raw one
            return original_decorator(wrapped)

        return new_decorator

    klein.Klein.route = patched_route
