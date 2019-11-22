import requests
import pytest
from apistar import TestClient
from api.web.support import Status
from tests.markers import smoke


@pytest.fixture(scope="module")
def response(client: TestClient) -> requests.Response:
    return client.get("/rest")


@smoke
def test_get_vehicles_status(response: requests.Response) -> None:
    assert response.status_code == Status.SUCCESS.code


@smoke
def test_vehicles_count(response: requests.Response) -> None:
    assert len(response.json()) == 1000


@smoke
def test_vehicles_is_list(response: requests.Response) -> None:
    assert type(response.json()) is list


@smoke
def test_get_first_vehicle(response: requests.Response) -> None:
    assert response.json()[0] == {
        "id_": 1,
        "manufacturer": "Mazda",
        "model": "RX-8",
        "year": 2006,
        "vin": "JTJBARBZ2F2356837",
    }


@smoke
def test_last_vehicle_id(response: requests.Response) -> None:
    assert response.json()[-1]["id_"] == 1000
