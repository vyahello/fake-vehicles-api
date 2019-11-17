from typing import Dict, Any, Set, List
from api.data.converter import to_dict
from api.data.files import File, TextFile, safe_file_of
from apistar.types import Type
from apistar.validators import Integer, String

StorageType = Dict[int, Dict[Any, Any]]


def _load_vehicles(storage: str) -> StorageType:
    """Loads data storage of cars."""
    with TextFile(storage, mode="r") as file:  # type: File
        return {next_car["id_"]: next_car for next_car in to_dict(file.read())}


class Vehicle(Type):
    """The class represents a single vehicle.

    Please be aware that it contains data type validation under the hood (from `Type` class).
    """

    id_: Integer = Integer(allow_null=True)
    manufacturer: String = String(max_length=30)
    model: String = String(max_length=30)
    year: Integer = Integer(minimum=1900, maximum=2050)
    vin: String = String(max_length=50, default="")


class VehicleStorage:
    """The class represents a storage of cars."""

    def __init__(self, storage_path: str) -> None:
        self._storage: StorageType = _load_vehicles(safe_file_of(storage_path, extensions=("json",)))

    def list_vehicles(self) -> List[Vehicle]:
        """Loads data storage of cars."""
        return list(map(lambda vehicle: Vehicle(vehicle[1]), sorted(self._storage.items())))

    def list_manufacturers(self) -> Set[str]:
        """Returns unique list of manufacturers."""
        return set(next_car["manufacturer"] for next_car in self._storage.values())
