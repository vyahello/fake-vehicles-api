"""The module contains API for data converters."""
# pylint:disable=c-extension-no-member
from typing import Dict, Any, List, Union
import ujson

_JsonType = Union[List[Any], Dict[Any, Any]]


def to_dict(data: str) -> Dict[Any, Any]:
    """Converts given stream into a `dict` schema."""
    return ujson.loads(data)


def to_str(data: _JsonType) -> str:
    """Converts given data into a `str` schema."""
    return ujson.dumps(data)
