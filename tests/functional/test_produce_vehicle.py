import pytest
import requests
from apistar import TestClient
from api import list_of_vehicles
from api.web.support import Status
from tests.markers import smoke


@pytest.fixture(scope="module")
def response(client: TestClient) -> requests.Response:
    return client.post("/", data={"manufacturer": "BMW", "model": "X5", "year": 2011, "vin": "WBAWV53589P465532"})


@smoke
def test_create_vehicle_status(response: requests.Response) -> None:
    assert response.status_code == Status.CREATED.code


@smoke
def test_count_vehicles(response: requests.Response) -> None:
    assert len(list_of_vehicles) == 1001
