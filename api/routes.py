from typing import List
from apistar.http import JSONResponse
from api import list_of_vehicles
from api.vehicle.vehicles import Vehicle
from api.web.support import Status


def list_vehicles() -> List[Vehicle]:
    """Returns a list of vehicles.

    Operates "/" route on "GET" request e.g "http://127.0.0.1:5000/".
    """
    return list(map(lambda vehicle: Vehicle(vehicle[1]), sorted(list_of_vehicles.items())))


def create_vehicle(vehicle: Vehicle) -> JSONResponse:
    """Creates a vehicle.

    Operates "/" route on "POST" request e.g "http://127.0.0.1:5000/".
    Passes following body structure sample:
    ```
        {
            "manufacturer": "BMW",
            "model": "X5",
            "year": 2011,
            "vin": "WBAWV53589P465532"
        }
    ```

    Args:
        vehicle: a vehicle

    Returns:
        http json response
    """
    vehicle.id_ = len(list_of_vehicles) + 1
    list_of_vehicles[vehicle.id_] = vehicle
    return JSONResponse(vehicle, status_code=Status.CREATED.code)
