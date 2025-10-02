import inspect
import sysconfig
from typing import Any, Callable, Optional, Set

_stdlib = sysconfig.get_paths()["stdlib"]


_ATTR_CANDIDATES = (
    "resolver",
    "func",
    "python_func",
    "_resolver",
    "wrapped_func",
    "__func",
)


def _is_user_code(path: Optional[str] = None) -> bool:
    return (
        bool(path)
        and not path.startswith(_stdlib)
        and "site-packages" not in path
        and "dist-packages" not in path
        and not path.startswith("<")
    )


def _unwrap_user_func(fn: Callable[..., Any]) -> Callable[..., Any]:
    """Unwrap decorators & closures until we find your user function."""
    seen: Set[int] = set()
    queue = [fn]
    while queue:
        current = queue.pop()
        if id(current) in seen:
            continue
        seen.add(id(current))

        if inspect.isfunction(current) and _is_user_code(current.__code__.co_filename):
            return current

        inner = getattr(current, "__wrapped__", None)
        if inner:
            queue.append(inner)

        for attr in _ATTR_CANDIDATES:
            attr_val = getattr(current, attr, None)
            if inspect.isfunction(attr_val):
                queue.append(attr_val)

        for cell in getattr(current, "__closure__", []) or []:
            cc = cell.cell_contents
            if inspect.isfunction(cc):
                queue.append(cc)

    return fn  # fallback
