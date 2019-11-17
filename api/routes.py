from typing import List
from api import list_of_vehicles
from api.vehicle.vehicles import Vehicle


def list_vehicles() -> List[Vehicle]:
    """Returns a list of vehicles.

    Operates "/" route on "GET" request e.g "http://127.0.0.1:5000/".
    """
    return list(map(lambda vehicle: Vehicle(vehicle[1]), sorted(list_of_vehicles.items())))
