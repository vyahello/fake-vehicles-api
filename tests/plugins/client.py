import pytest
from api.app import api_app
from apistar import TestClient


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(api_app)
