import pytest
import requests
from apistar import TestClient
from api import list_of_vehicles
from api.web.support import Status
from tests.markers import smoke

_initial_count: int = len(list_of_vehicles)


@pytest.fixture(scope="module")
def response(client: TestClient) -> requests.Response:
    return client.delete("/10")


@pytest.fixture(scope="module")
def response_error(client: TestClient) -> requests.Response:
    return client.get("/10")


@smoke
def test_delete_vehicle_status(response: requests.Response) -> None:
    assert response.status_code == Status.NO_CONTENT.code


@smoke
def test_delete_vehicle_status(response: requests.Response) -> None:
    assert response.json() == {}


@smoke
def test_count_vehicles(client: TestClient) -> None:
    assert len(client.get("/").json()) == _initial_count


@smoke
def test_vehicle_not_found_status(response_error: requests.Response) -> None:
    assert response_error.status_code == Status.NOT_FOUND.code


@smoke
def test_vehicle_not_found_content(response_error: requests.Response) -> None:
    assert response_error.json() == {"error": "vehicle not found"}
