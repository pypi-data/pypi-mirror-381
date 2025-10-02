import threading
from concurrent.futures import Future
from contextvars import copy_context
from typing import Optional

import requests

from .env_vars import SF_DEBUG
from .server_status import server_running
from .shutdown_flag import is_shutting_down
from .thread_local import _thread_locals, suppress_network_recording


def get_header(request, header_name):
    return request.headers.get(header_name)


def set_header(request, header_name, header_value):
    request.headers[header_name] = header_value


def is_server_running(url="http://localhost:8000/healthz"):
    global server_running
    if server_running:
        return True

    try:
        with suppress_network_recording():
            response = requests.get(url, timeout=1)
        if response.status_code == 200:
            server_running = True
            return True
    except requests.RequestException:
        pass
    return False


def non_blocking_post(url, operation_name, query, variables) -> Future:
    global is_shutting_down

    if is_shutting_down:
        return None

    if (
        hasattr(_thread_locals, "reentrancy_guard_logging_preactive")
        and _thread_locals.reentrancy_guard_logging_preactive
    ):
        variables["reentrancyGuardPreactive"] = True
    if SF_DEBUG:
        print(
            f"******* Sending data to {url}: query={query}, variables={variables}, operation_name={operation_name}",
            log=False,
        )

    # # Sibyl - Disable to allow for posts to always run
    # if not is_server_running():
    #     return

    def post() -> Optional[dict]:
        try:
            with suppress_network_recording():
                response = requests.post(
                    url,
                    headers={"Content-Type": "application/json"},
                    json={
                        "query": query,
                        "variables": variables,
                        "operationName": operation_name,
                    },
                    timeout=10,
                )
            if SF_DEBUG:
                print(
                    "POSTED!!",
                    "operation_name",
                    operation_name,
                    "query",
                    query,
                    response.json(),
                    log=False,
                )
            if response.status_code != 200:
                return
            return response.json()
        except Exception as e:  # Broad exception handling for debugging
            if SF_DEBUG:
                print(f"POST request failed to {url}: {e}", log=False)

    future = Future()
    ctx = copy_context()

    if SF_DEBUG:
        # Directly call post for debugging and set the result in the Future
        result = post()
        future.set_result(result)
    else:
        # For non-debug mode, run post in a thread and set the result in the Future
        def wrapper():
            result = post()
            future.set_result(result)

        threading.Thread(target=wrapper).start()

    return future
