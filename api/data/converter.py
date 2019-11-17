"""The module contains API for data converters."""
from typing import Dict, Any, List, Union
import ujson as json

_JsonType = Union[List[Any], Dict[Any, Any]]


def to_dict(data: str) -> Dict[Any, Any]:
    """Converts given stream into a `dict` schema."""
    return json.loads(data)


def to_str(data: _JsonType) -> str:
    """Converts given data into a `str` schema."""
    return json.dumps(data)
