import logging
from typing import Any

from cattle_grid.model import ActivityMessage

from muck_out.types import Activity, Actor, Object, Collection

logger = logging.getLogger(__name__)


def data_to_type(data: dict[str, Any], key: str, object_type) -> None:
    try:
        candidate = data.get("parsed", {}).get(key)
        if not candidate:
            return None
        return object_type.model_validate(candidate)
    except Exception as e:
        logger.info(e)
        return None


def get_activity(message: ActivityMessage) -> None | Activity:
    return data_to_type(message.data, "activity", Activity)


def get_actor(message: ActivityMessage) -> None | Actor:
    return data_to_type(message.data, "actor", Actor)


def get_object(message: ActivityMessage) -> None | Object:
    return data_to_type(message.data, "object", Object)


def get_embedded_object(message: ActivityMessage) -> None | Object:
    return data_to_type(message.data, "embedded_object", Object)


def get_collection(message: ActivityMessage) -> None | Collection:
    return data_to_type(message.data, "collection", Collection)
