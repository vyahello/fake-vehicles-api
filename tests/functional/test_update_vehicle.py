import pytest
import requests
from apistar import TestClient
from api.web.support import Status

_data = {"id_": 9, "manufacturer": "Audi", "model": "S8", "year": 2002, "vin": "SAJWA4DC3FM713027"}


@pytest.fixture(scope="module")
def response_success(client: TestClient) -> requests.Response:
    return client.put("/9", data=_data)


@pytest.fixture(scope="module")
def response_error(client: TestClient) -> requests.Response:
    return client.put("/9999", data=_data)


@pytest.fixture(scope="module")
def response_validation(client: TestClient) -> requests.Response:
    return client.put("/9999", data={"manufacturer": "A" * 51, "model": "S" * 51, "year": 1899})


def test_update_vehicle_status(response_success: requests.Response) -> None:
    assert response_success.status_code == Status.SUCCESS.code


def test_update_vehicle_content(response_success: requests.Response) -> None:
    assert response_success.json() == _data


def test_update_error_vehicle_status(response_error: requests.Response) -> None:
    assert response_error.status_code == Status.NOT_FOUND.code


def test_update_error_vehicle_content(response_error: requests.Response) -> None:
    assert response_error.json() == {"error": "vehicle not found"}


def test_manufacturer_validation(response_validation: requests.Response) -> None:
    assert "Must be one of" in response_validation.json()["manufacturer"]


def test_model_validation(response_validation: requests.Response) -> None:
    assert response_validation.json()["model"] == "Must have no more than 30 characters."


def test_year_validation(response_validation: requests.Response) -> None:
    assert response_validation.json()["year"] == "Must be greater than or equal to 1900."
