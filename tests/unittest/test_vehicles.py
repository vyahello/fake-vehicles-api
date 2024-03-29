import os
import pytest
from apistar.exceptions import ValidationError
from api.vehicle.storage import VehicleStorage, _load_vehicles
from api.data.files import File, TextFile
from api.vehicle.vehicles import Vehicle
from tests.markers import unittest

_name: str = "file.json"


@pytest.fixture(scope="module", autouse=True)
def setup() -> None:
    with TextFile(_name, mode="w") as file:  # type: File
        file.write(
            """
            [
                {"id_":1,"manufacturer":"Mazda","model":"RX-8","year":2006,"vin":"JTJBARBZ2F2356837"},
                {"id_":2,"manufacturer":"Honda","model":"Civic Si","year":2003,"vin":"1N6AF0LY0FN792678"}
            ]
            """
        )
    yield
    os.remove(_name)


@pytest.fixture(scope="module")
def storage() -> VehicleStorage:
    return VehicleStorage(_name)


@pytest.fixture(scope="module")
def vehicle() -> Vehicle:
    return Vehicle({"id_": 1, "manufacturer": "Mazda", "model": "RX-8", "year": 2006, "vin": "JTJBARBZ2F2356837"})


@unittest
def test_load_vehicles() -> None:
    assert _load_vehicles(_name) == {
        1: {"id_": 1, "manufacturer": "Mazda", "model": "RX-8", "year": 2006, "vin": "JTJBARBZ2F2356837"},
        2: {"id_": 2, "manufacturer": "Honda", "model": "Civic Si", "year": 2003, "vin": "1N6AF0LY0FN792678"},
    }


@unittest
def test_cars(storage: VehicleStorage) -> None:
    assert storage.list_vehicles() == {
        1: {"id_": 1, "manufacturer": "Mazda", "model": "RX-8", "year": 2006, "vin": "JTJBARBZ2F2356837"},
        2: {"id_": 2, "manufacturer": "Honda", "model": "Civic Si", "year": 2003, "vin": "1N6AF0LY0FN792678"},
    }


@unittest
def test_manufacturers(storage: VehicleStorage) -> None:
    assert storage.list_manufacturers() == {"Mazda", "Honda"}


@unittest
def test_vehicle_id(vehicle: Vehicle) -> None:
    assert vehicle.id_ == 1


@unittest
def test_vehicle_manufacturer(vehicle: Vehicle) -> None:
    assert vehicle.manufacturer == "Mazda"


@unittest
def test_vehicle_model(vehicle: Vehicle) -> None:
    assert vehicle.model == "RX-8"


@unittest
def test_vehicle_year(vehicle: Vehicle) -> None:
    assert vehicle.year == 2006


@unittest
def test_vehicle_vin(vehicle: Vehicle) -> None:
    assert vehicle.vin == "JTJBARBZ2F2356837"


@unittest
def test_vehicle_null_id(vehicle: Vehicle) -> None:
    Vehicle({"manufacturer": "Mazda", "model": "R", "year": 2000, "vin": "some_vin"})


@unittest
def test_vehicle_wrong_manufacturer(vehicle: Vehicle) -> None:
    with pytest.raises(ValidationError):
        Vehicle({"manufacturer": "M", "model": "R", "year": 2000, "vin": "some_vin"})


@unittest
def test_vehicle_wrong_model(vehicle: Vehicle) -> None:
    with pytest.raises(ValidationError):
        Vehicle({"manufacturer": "Mazda", "model": "R" * 31, "year": 2000, "vin": "some_vin"})


@unittest
def test_vehicle_wrong_year(vehicle: Vehicle) -> None:
    with pytest.raises(ValidationError):
        Vehicle({"manufacturer": "Mazda", "model": "R", "year": 1899, "vin": "some_vin"})


@unittest
def test_vehicle_wrong_vin(vehicle: Vehicle) -> None:
    with pytest.raises(ValidationError):
        Vehicle({"manufacturer": "Mazda", "model": "R", "year": 2000, "vin": "v" * 51})
