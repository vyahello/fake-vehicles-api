import os
import pytest
from _pytest.fixtures import SubRequest
from api.data.files import safe_file_of, File, TextFile
from tests.markers import unittest

_name: str = "file.txt"
_input: str = "data"


@pytest.fixture(scope="module", autouse=True)
def remove_file(request: SubRequest) -> None:
    request.addfinalizer(lambda: os.remove(_name))


@unittest
def test_write_file() -> None:
    with TextFile(_name, mode="w") as file:  # type: File
        file.write(_input)


@unittest
def test_read_file() -> None:
    with TextFile(_name, mode="r") as file:  # type: File
        assert file.read() == _input


@unittest
def test_safe_file_of() -> None:
    assert safe_file_of(_name, extensions=("txt",))


@unittest
def test_not_safe_file_of() -> None:
    with pytest.raises(ValueError):
        safe_file_of(_name, extensions=("json",))
