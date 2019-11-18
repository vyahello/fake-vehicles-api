from dataclasses import FrozenInstanceError
import pytest
from api.app import Setup
from tests.markers import unittest


@pytest.fixture(scope="module", autouse=True)
def setup() -> Setup:
    return Setup(host="name", port=7878, debug=True)


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
def test_frozen_setup(setup: Setup) -> None:
    with pytest.raises(FrozenInstanceError):
        setup.debug = False
