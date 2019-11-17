import os
import pytest
from _pytest.fixtures import SubRequest
from api.data.files import File, TextFile

_name: str = "file.txt"
_input: str = "data"


@pytest.fixture(scope="module", autouse=True)
def remove_file(request: SubRequest) -> None:
    request.addfinalizer(lambda: os.remove(_name))


def test_write_file() -> None:
    with TextFile(_name, mode="w") as file:  # type: File
        file.write(_input)


def test_read_file() -> None:
    with TextFile(_name, mode="r") as file:  # type: File
        assert file.read() == _input
