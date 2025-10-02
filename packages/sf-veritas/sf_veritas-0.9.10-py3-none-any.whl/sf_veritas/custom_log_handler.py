import logging
from typing import Optional

from . import app_config
from .env_vars import PRINT_CONFIGURATION_STATUSES, SF_DEBUG
from .interceptors import LogInterceptor
from .thread_local import get_or_set_sf_trace_id


class CustomLogHandler(logging.Handler, LogInterceptor):
    def __init__(self):
        logging.Handler.__init__(self)
        LogInterceptor.__init__(self, api_key=app_config._sailfish_api_key)
        if PRINT_CONFIGURATION_STATUSES:
            print("Intercepting log statements")

    def emit(self, record, trace_id: Optional[str] = None):
        if isinstance(record, logging.LogRecord):
            try:
                log_entry = self.format(record)
                log_level = record.levelname

                if SF_DEBUG:
                    print(
                        "[[DEBUG custom_log_handler]]",
                        f"trace_id={trace_id}",
                        f"[[{log_level}]]",
                        log_entry,
                        "[[/DEBUG]]",
                        log=False,
                    )

                if SF_DEBUG:
                    print(
                        "CustomLogHandler...SENDING DATA...do_send args=",
                        (log_level, log_entry, trace_id),
                        trace_id,
                        log=False,
                    )
                _, trace_id = get_or_set_sf_trace_id(trace_id)
                if SF_DEBUG:
                    print(
                        "CustomLogHandler...SENDING DATA...do_send args=",
                        (log_level, log_entry, trace_id),
                        trace_id,
                        log=False,
                    )
                self.do_send((log_level, log_entry, trace_id), trace_id)

            except Exception as e:  # pylint: disable=broad-exception-caught
                # TODO - Sibyl post-launch - disable this print??
                print("There's an error when emitting!!!!!\n", e)
                self.handleError(record)
