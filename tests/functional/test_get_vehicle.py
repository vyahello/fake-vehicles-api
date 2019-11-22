import pytest
import requests
from apistar import TestClient
from api.web.support import Status
from tests.markers import smoke


@pytest.fixture(scope="module")
def response_success(client: TestClient) -> requests.Response:
    return client.get("/api/10")


@pytest.fixture(scope="module")
def response_error(client: TestClient) -> requests.Response:
    return client.get("/api/9999")


@smoke
def test_get_car_success_status(response_success: requests.Response) -> None:
    assert response_success.status_code == Status.SUCCESS.code


@smoke
def test_get_car_success_content(response_success: requests.Response) -> None:
    assert response_success.json() == {
        "id_": 10,
        "manufacturer": "Kia",
        "model": "Sportage",
        "year": 2011,
        "vin": "3C6TD5GT0CG557688",
    }


@smoke
def test_get_car_error_status(response_error: requests.Response) -> None:
    assert response_error.status_code == Status.NOT_FOUND.code


@smoke
def test_get_car_error_content(response_error: requests.Response) -> None:
    assert response_error.json() == {"error": "vehicle not found"}
