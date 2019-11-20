from typing import List
from apistar.http import JSONResponse
from api import list_of_vehicles
from api.vehicle.vehicles import Vehicle
from api.web.support import Status

_error_response: JSONResponse = JSONResponse(content={"error": "vehicle not found"}, status_code=Status.NOT_FOUND.code)


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


def get_vehicle(vehicle_id: int) -> JSONResponse:
    """Gets single vehicle.

    Operates "/{id}" route on "GET" request e.g "http://127.0.0.1:5000/99".

    Args:
        vehicle_id: a vehicle ID e.g `2`

    Returns:
        http json response
    """
    vehicle: Vehicle = list_of_vehicles.get(vehicle_id)
    if not vehicle:
        return _error_response
    return JSONResponse(vehicle, status_code=Status.SUCCESS.code)


def update_vehicle(vehicle_id: int, vehicle: Vehicle) -> JSONResponse:
    """Updates vehicle by it's ID.

    Operates "/{id}" route on "PUT" request e.g "http://127.0.0.1:5000/99".

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
        vehicle_id: vehicle ID e.g `2`
        vehicle: a vehicle item

    Returns:
        http json response
    """
    if not list_of_vehicles.get(vehicle_id):
        return _error_response
    vehicle.id_ = vehicle_id
    list_of_vehicles[vehicle_id] = vehicle
    return JSONResponse(vehicle, status_code=Status.SUCCESS.code)
