from typing import Dict, Any, Set
from api.data.converter import to_dict
from api.data.files import File, TextFile, safe_file_of

StorageType = Dict[int, Dict[Any, Any]]


def _load_vehicles(storage: str) -> StorageType:
    """Loads data storage of cars."""
    with TextFile(storage, mode="r") as file:  # type: File
        return {next_car["id_"]: next_car for next_car in to_dict(file.read())}


class VehicleStorage:
    """The class represents a storage of cars."""

    def __init__(self, storage_path: str) -> None:
        self._storage: StorageType = _load_vehicles(safe_file_of(storage_path, extensions=("json",)))

    def list_vehicles(self) -> StorageType:
        """Loads data storage of cars."""
        return self._storage

    def list_manufacturers(self) -> Set[str]:
        """Returns unique list of manufacturers."""
        return set(next_car["manufacturer"] for next_car in self._storage.values())
