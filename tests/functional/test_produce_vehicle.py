import pytest
import requests
from apistar import TestClient
from api import list_of_vehicles
from api.web.support import Status
from tests.markers import smoke


@pytest.fixture(scope="module")
def response_success(client: TestClient) -> requests.Response:
    return client.post("/rest", data={"manufacturer": "BMW", "model": "X5", "year": 2011, "vin": "WBAWV53589P465532"})


@pytest.fixture(scope="module")
def response_missing_fields(client: TestClient) -> requests.Response:
    return client.post("/rest", data={"foo": "bar"})


@pytest.fixture(scope="module")
def response_fields_validation(client: TestClient) -> requests.Response:
    return client.post("/rest", data={"manufacturer": "A" * 51, "model": "A" * 51, "year": 2051})


@smoke
def test_create_vehicle_status(response_success: requests.Response) -> None:
    assert response_success.status_code == Status.CREATED.code


@smoke
def test_count_vehicles(response_success: requests.Response) -> None:
    assert len(list_of_vehicles) == 1001


@smoke
def test_missing_manufacturer(response_missing_fields: requests.Response) -> None:
    assert response_missing_fields.json()["manufacturer"] == 'The "manufacturer" field is required.'


@smoke
def test_missing_model(response_missing_fields: requests.Response) -> None:
    assert response_missing_fields.json()["model"] == 'The "model" field is required.'


@smoke
def test_missing_year(response_missing_fields: requests.Response) -> None:
    assert response_missing_fields.json()["year"] == 'The "year" field is required.'


@smoke
def test_manufacturer_validation(response_fields_validation: requests.Response) -> None:
    assert "Must be one of" in response_fields_validation.json()["manufacturer"]


@smoke
def test_model_validation(response_fields_validation: requests.Response) -> None:
    assert response_fields_validation.json()["model"] == "Must have no more than 30 characters."


@smoke
def test_year_validation(response_fields_validation: requests.Response) -> None:
    assert response_fields_validation.json()["year"] == "Must be less than or equal to 2050."
