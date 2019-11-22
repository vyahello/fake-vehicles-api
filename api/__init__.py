import os
from typing import List, Dict, Any
from api.setup import MoveTo, Setup
from api.vehicle.storage import VehicleStorage

if os.path.basename(os.getcwd()) == "api":
    os.chdir("../")


move_to: MoveTo = MoveTo()
setup: Setup = Setup()
storage = VehicleStorage(os.path.join(os.getcwd(), "api/data/vehicles.json"))
list_of_vehicles: Dict[int, Any] = storage.list_vehicles()
LIST_OF_MANUFACTURERS: List[str] = list(storage.list_manufacturers())
