import pytest
import requests
from apistar import TestClient

from api.web.support import Status


@pytest.fixture(scope="module")
def response_home(client: TestClient) -> requests.Response:
    return client.get("/")


@pytest.fixture(scope="module")
def response_index(client: TestClient) -> requests.Response:
    return client.get("/index.html")


def test_home_status_code(response_home: requests.Response) -> None:
    assert response_home.status_code == Status.SUCCESS.code


def test_home_status_content(response_home: requests.Response) -> None:
    assert "Fake vehicles" in response_home.text


def test_index_status_code(response_index: requests.Response) -> None:
    assert response_index.status_code == Status.SUCCESS.code


def test_index_status_content(response_index: requests.Response) -> None:
    assert "Fake vehicles" in response_index.text
