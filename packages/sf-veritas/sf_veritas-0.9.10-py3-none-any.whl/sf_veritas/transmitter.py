from typing import Any, Dict, Optional

from .env_vars import SF_DEBUG
from .interceptors import CollectMetadataTransmitter
from .thread_local import get_or_set_sf_trace_id

collect_metadata_transmitter = CollectMetadataTransmitter()


class SailfishTransmitter(object):
    @classmethod
    def identify(
        cls,
        user_id: str,
        traits: Optional[Dict[str, Any]] = None,
        traits_json: Optional[str] = None,
        override: bool = False,
    ) -> None:
        if traits is not None or traits_json is not None:
            return cls.add_or_update_metadata(user_id, traits, traits_json, override)
        return cls.add_or_update_metadata(user_id, dict(), override=override)

    @classmethod
    def add_or_update_metadata(
        cls,
        user_id: str,
        traits: Optional[Dict[str, Any]] = None,
        traits_json: Optional[str] = None,
        override: bool = False,
    ) -> None:
        """
        Sets traits and sends to the Sailfish AI backend

        Args:
            user_id: unique identifier for the user; common uses are username or email
            traits: dictionary of contents to add or update in the user's traits. Defaults to None.
            traits_json: json string of contents to add or update in the user's traits. Defaults to None.
        """
        if traits is None and traits_json is None:
            raise Exception(
                'Must pass in either traits or traits_json to "add_or_update_traits"'
            )
        if SF_DEBUG:
            print(
                "[[DEBUG - add_or_update_traits]] starting thread [[/DEBUG]]", log=False
            )

        _, trace_id = get_or_set_sf_trace_id()
        if SF_DEBUG:
            print(
                "add_or_update_metadata...SENDING DATA...args=",
                (user_id, traits, traits_json, override, trace_id),
                trace_id,
                log=False,
            )
        collect_metadata_transmitter.do_send(
            (user_id, traits, traits_json, override, trace_id), trace_id
        )
