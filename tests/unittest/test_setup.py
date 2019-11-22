from dataclasses import FrozenInstanceError
import pytest
from api.setup import Setup, _Directory
from tests.markers import unittest


@pytest.fixture(scope="module", autouse=True)
def setup() -> Setup:
    return Setup(host="name", port=7878, debug=True)


@pytest.fixture(scope="module", autouse=True)
def dir_() -> _Directory:
    return _Directory("A", "B")


@unittest
def test_setup_host(setup: Setup) -> None:
    assert setup.host == "name"


@unittest
def test_setup_port(setup: Setup) -> None:
    assert setup.port == 7878


@unittest
def test_setup_debug(setup: Setup) -> None:
    assert setup.debug


@unittest
def test_setup_dir(setup: Setup) -> None:
    assert isinstance(setup.dir_, _Directory)


@unittest
def test_frozen_setup(setup: Setup) -> None:
    with pytest.raises(FrozenInstanceError):
        setup.debug = False


def test_dir_templates(dir_: _Directory) -> None:
    assert dir_.templates == "A"


def test_dir_static(dir_: _Directory) -> None:
    assert dir_.static == "B"


@unittest
def test_frozen_dir(dir_: _Directory) -> None:
    with pytest.raises(FrozenInstanceError):
        dir_.templates = False
