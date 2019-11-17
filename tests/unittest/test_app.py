import pytest
from api.app import Setup
from tests.markers import unittest


@pytest.fixture(scope="module", autouse=True)
def setup() -> Setup:
    return Setup(host="name", port=7878)


@unittest
def test_setup_host(setup: Setup) -> None:
    assert setup.host == "name"


@unittest
def test_setup_port(setup: Setup) -> None:
    assert setup.port == 7878
