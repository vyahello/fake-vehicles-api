from typing import List, Dict, Any
from api.vehicle.storage import VehicleStorage

storage = VehicleStorage(storage_path="api/data/vehicles.json")

list_of_vehicles: Dict[int, Any] = storage.list_vehicles()
LIST_OF_MANUFACTURERS: List[str] = list(storage.list_manufacturers())
