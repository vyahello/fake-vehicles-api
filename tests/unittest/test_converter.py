from typing import Dict, List
from api.data.converter import to_str, to_dict

_string: str = '[{"a":1},{"b":2}]'
_json: List[Dict[str, int]] = [{"a": 1}, {"b": 2}]


def test_to_dict() -> None:
    assert to_dict(_string) == _json


def test_to_str() -> None:
    assert to_str(_json) == _string
