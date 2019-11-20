import os
from typing import List, Dict, Any
from api.vehicle.storage import VehicleStorage


def _storage() -> VehicleStorage:
    """Returns storage for vehicles."""
    if os.path.basename(os.getcwd()) != "api":
        return VehicleStorage(os.path.join(os.getcwd(), "api/data/vehicles.json"))
    return VehicleStorage(os.path.join(os.getcwd(), "data/vehicles.json"))


list_of_vehicles: Dict[int, Any] = _storage().list_vehicles()
LIST_OF_MANUFACTURERS: List[str] = list(_storage().list_manufacturers())
