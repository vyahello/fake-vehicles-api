from typing import List, Optional
from apistar import App, Route
from apistar.http import JSONResponse
from api import list_of_vehicles, move_to, setup
from api.vehicle.vehicles import Vehicle
from api.web.support import Method, Status, RESPONSE_ERROR


def home() -> str:
    """Return welcome page."""
    return api_app.render_template("home/index.html")


def list_vehicles() -> List[Vehicle]:
    """Returns a list of vehicles.

    Operates "/rest" route on "GET" request e.g "http://127.0.0.1:5000/rest".
    """
    return list(map(lambda vehicle: Vehicle(vehicle[1]), sorted(list_of_vehicles.items())))


def create_vehicle(vehicle: Vehicle) -> JSONResponse:
    """Creates a vehicle.

    Operates "/rest" route on "POST" request e.g "http://127.0.0.1:5000/rest".
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

    Operates "/rest/{id}" route on "GET" request e.g "http://127.0.0.1:5000/rest/99".

    Args:
        vehicle_id: a vehicle ID e.g `2`

    Returns:
        http json response
    """
    vehicle: Optional[Vehicle] = list_of_vehicles.get(vehicle_id)
    if not vehicle:
        return RESPONSE_ERROR
    return JSONResponse(vehicle, status_code=Status.SUCCESS.code)


def update_vehicle(vehicle_id: int, vehicle: Vehicle) -> JSONResponse:
    """Updates vehicle by it's ID.

    Operates "/rest/{id}" route on "PUT" request e.g "http://127.0.0.1:5000/rest/99".

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
        return RESPONSE_ERROR
    vehicle.id_ = vehicle_id
    list_of_vehicles[vehicle_id] = vehicle
    return JSONResponse(vehicle, status_code=Status.SUCCESS.code)


def delete_vehicle(vehicle_id: int) -> JSONResponse:
    """Deletes vehicle by it's id.

    Operates "/rest/{id}" route on "DELETE" request e.g "http://127.0.0.1:5000/rest/99"

    Args:
        vehicle_id: vehicle ID

    Returns:
        http json response
    """
    if not list_of_vehicles.get(vehicle_id):
        return RESPONSE_ERROR
    del list_of_vehicles[vehicle_id]
    return JSONResponse({}, status_code=Status.NO_CONTENT.code)


ROUTES = [
    Route(move_to.home, method=Method.GET.name, handler=home),
    Route(move_to.index, method=Method.GET.name, handler=lambda: home()),  # pylint:disable=unnecessary-lambda
    Route(move_to.root, method=Method.GET.name, handler=list_vehicles),
    Route(move_to.root, method=Method.POST.name, handler=create_vehicle),
    Route(move_to.id_, method=Method.GET.name, handler=get_vehicle),
    Route(move_to.id_, method=Method.PUT.name, handler=update_vehicle),
    Route(move_to.id_, method=Method.DELETE.name, handler=delete_vehicle),
]
api_app: App = App(ROUTES, setup.dir_.templates, setup.dir_.static)


if __name__ == "__main__":
    api_app.serve(setup.host, setup.port, True)
