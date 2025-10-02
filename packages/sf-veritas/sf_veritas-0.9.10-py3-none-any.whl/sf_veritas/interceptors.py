import json
import logging
import re
import threading
import time
import uuid
from typing import Any, Dict, List, Optional

from . import app_config
from .env_vars import SF_DEBUG
from .package_metadata import PACKAGE_LIBRARY_TYPE, __version__
from .regular_data_transmitter import ServiceIdentifier
from .request_utils import non_blocking_post
from .thread_local import (  # reentrancy_guard, activate_reentrancy_guards_logging_preactive,
    activate_reentrancy_guards_logging,
    get_or_set_sf_trace_id,
)
from .timeutil import TimeSync
from .types import CustomJSONEncoderForFrameInfo, FrameInfo
from .utils import serialize_json_with_exclusions, strtobool

logger = logging.getLogger(__name__)


class OutputInterceptor(object):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or app_config._sailfish_api_key
        self.endpoint = app_config._sailfish_graphql_endpoint
        self.operation_name: Optional[str] = ""
        self.query_type = "mutation"
        self.service_identifier = ServiceIdentifier()

    @property
    def query_name(self) -> str:
        return (
            self.operation_name[0].lower() + self.operation_name[1:]
            if self.operation_name
            else ""
        )

    def get_default_variables(self, session_id: Optional[str] = None):
        trace_id = session_id
        if not session_id:
            _, trace_id = get_or_set_sf_trace_id(session_id)
        timestamp_ms = TimeSync.get_instance().get_utc_time_in_ms()
        return {
            "apiKey": self.api_key,
            "serviceUuid": app_config._service_uuid,
            "library": PACKAGE_LIBRARY_TYPE,
            "sessionId": trace_id,
            "timestampMs": str(timestamp_ms),
            "version": __version__,
        }

    def get_variables(
        self,
        additional_variables: Optional[Dict[str, Any]] = None,
        session_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        additional_variables = (
            additional_variables if additional_variables is not None else {}
        )
        return {
            **additional_variables,
            **self.get_default_variables(session_id),
        }

    def check_if_contents_should_be_ignored(
        self, contents
    ):  # pylint: disable=unused-argument
        return False

    def _send_app_identifier(self, session_id: str) -> None:
        if SF_DEBUG:
            print(
                "_send_app_identifier...SENDING DATA...args=",
                set(),
                log=False,
            )
        self.service_identifier.do_send(set())

    def do_send(self, args, session_id: str) -> None:
        self._send_app_identifier(session_id)
        if SF_DEBUG:
            print(f"[[OutputInterceptor.do_send]] session_id={session_id}", log=False)
        try:
            threading.Thread(target=self.send, args=args).start()
        except RuntimeError:
            return


class LogInterceptor(OutputInterceptor):
    def __init__(self, api_key: str = app_config._sailfish_api_key):
        super().__init__(api_key)
        self.operation_name = "CollectLogs"

    def check_if_contents_should_be_ignored(self, contents):
        if SF_DEBUG:
            print(
                "LogInterceptor...check_if_contents_should_be_ignored(self, contents)",
                "||||",
                contents,
                "||||",
                log=False,
            )
        pattern = r"HTTP\s(POST|GET)\s(\/healthz|\/graphql\/)\s.*"
        result = re.match(pattern, contents)
        return result is not None

    def send(
        self, level, contents, session_id: str
    ):  # pylint: disable=arguments-differ
        if SF_DEBUG:
            print(f"LogInterceptor:  Running send, session_id={session_id}", log=False)
        if self.check_if_contents_should_be_ignored(contents):
            if SF_DEBUG:
                print("LogInterceptor:  EARLY EXIT - contents:", contents, log=False)
            return
        query = f"""
        {self.query_type} {self.operation_name}($apiKey: String!, $serviceUuid: String!, $sessionId: String!, $level: String!, $contents: String!, $reentrancyGuardPreactive: Boolean!, $library: String!, $timestampMs: String!, $version: String!) {{
            {self.query_name}(apiKey: $apiKey, serviceUuid: $serviceUuid, sessionId: $sessionId, level: $level, contents: $contents, reentrancyGuardPreactive: $reentrancyGuardPreactive, library: $library, timestampMs: $timestampMs, version: $version)
        }}
        """
        if SF_DEBUG:
            print(
                "LogInterceptor:  non_blocking_post is next",
                "level",
                level,
                "contents:",
                contents,
                log=False,
            )
        non_blocking_post(
            self.endpoint,
            self.operation_name,
            query,
            self.get_variables(
                {
                    "level": level if level else "UNKNOWN",
                    "contents": contents,
                    "reentrancyGuardPreactive": False,
                },
                session_id,
            ),
        )


class PrintInterceptor(OutputInterceptor):
    def __init__(self, api_key: str = app_config._sailfish_api_key):
        super().__init__(api_key)
        self.operation_name = "CollectPrintStatements"

    def send(self, contents, session_id: str):
        if self.check_if_contents_should_be_ignored(contents):
            return
        query = f"""
        {self.query_type} {self.operation_name}($apiKey: String!, $serviceUuid: String!, $sessionId: String!, $contents: String!, $reentrancyGuardPreactive: Boolean!, $library: String!, $timestampMs: String!, $version: String!) {{
            {self.query_name}(apiKey: $apiKey, serviceUuid: $serviceUuid, sessionId: $sessionId, contents: $contents, reentrancyGuardPreactive: $reentrancyGuardPreactive, library: $library, timestampMs: $timestampMs, version: $version)
        }}
        """

        non_blocking_post(
            self.endpoint,
            self.operation_name,
            query,
            self.get_variables(
                {
                    "contents": contents,
                    "reentrancyGuardPreactive": False,
                },
                session_id,
            ),
        )


class ExceptionInterceptor(OutputInterceptor):
    def __init__(self, api_key: str = app_config._sailfish_api_key):
        super().__init__(api_key)
        self.operation_name = "CollectExceptions"

    def send(
        self,
        exception_message: str,
        trace: List[FrameInfo],
        session_id: str,
        was_caught: bool = True,
        is_from_local_service: bool = False
    ):
        query = f"""
        {self.query_type} {self.operation_name}($apiKey: String!, $serviceUuid: String!, $sessionId: String!, $exceptionMessage: String!, $wasCaught: Boolean!, $traceJson: String!, $reentrancyGuardPreactive: Boolean!, $library: String!, $timestampMs: String!, $version: String!, $isFromLocalService: Boolean!) {{
            {self.query_name}(apiKey: $apiKey, serviceUuid: $serviceUuid, sessionId: $sessionId, exceptionMessage: $exceptionMessage, wasCaught: $wasCaught, traceJson: $traceJson, reentrancyGuardPreactive: $reentrancyGuardPreactive, library: $library, timestampMs: $timestampMs, version: $version, isFromLocalService: $isFromLocalService)
        }}
        """

        if SF_DEBUG:
            print("SENDING EXCEPTION...", log=False)
        non_blocking_post(
            self.endpoint,
            self.operation_name,
            query,
            self.get_variables(
                {
                    "apiKey": self.api_key,
                    "exceptionMessage": exception_message,
                    "traceJson": json.dumps(trace, cls=CustomJSONEncoderForFrameInfo),
                    "reentrancyGuardPreactive": False,
                    "wasCaught": was_caught,
                    "isFromLocalService": is_from_local_service
                },
                session_id,
            ),
        )


class CollectMetadataTransmitter(OutputInterceptor):
    def __init__(self, api_key: str = app_config._sailfish_api_key):
        super().__init__(api_key)
        self.operation_name = "CollectMetadata"

    def send(
        self,
        user_id: str,
        traits: Optional[Dict[str, Any]],
        traits_json: Optional[str],
        override: bool,
        session_id: str,
    ):
        if traits is None and traits_json is None:
            raise Exception(
                'Must pass in either traits or traits_json to "add_or_update_traits"'
            )
        query = f"""
        {self.query_type} {self.operation_name}($apiKey: String!, $serviceUuid: String!, $sessionId: String!, $userId: String!, $traitsJson: String!, $excludedFields: [String!]!, $library: String!, $timestampMs: String!, $version: String!, $override: Boolean!) {{
            {self.query_name}(apiKey: $apiKey, serviceUuid: $serviceUuid, sessionId: $sessionId, userId: $userId, traitsJson: $traitsJson, excludedFields: $excludedFields, library: $library, timestampMs: $timestampMs, version: $version, override: $override)
        }}
        """

        excluded_fields = []
        if traits_json is None:
            traits_json, excluded_fields = serialize_json_with_exclusions(traits)

        variables = self.get_variables(
            {
                "userId": user_id,
                "traitsJson": traits_json,
                "excludedFields": excluded_fields,
                "override": override,
            },
            session_id,
        )

        non_blocking_post(self.endpoint, self.operation_name, query, variables)
