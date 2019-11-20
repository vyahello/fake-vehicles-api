from typing import List
from apistar import App, Route
from api.routes import index, list_vehicles, create_vehicle, get_vehicle, update_vehicle, delete_vehicle
from dataclasses import dataclass
from api.web.support import Method

_root: str = "/"
_index: str = "/index.html"
_id: str = "/{vehicle_id}"


@dataclass(frozen=True)
class Setup:
    """The class represents application setup."""

    host: str = "0.0.0.0"
    port: int = 5000
    debug: bool = False


_routes: List[Route] = [
    Route(_index, method=Method.GET.name, handler=index),
    Route(_root, method=Method.GET.name, handler=list_vehicles),
    Route(_root, method=Method.POST.name, handler=create_vehicle),
    Route(_id, method=Method.GET.name, handler=get_vehicle),
    Route(_id, method=Method.PUT.name, handler=update_vehicle),
    Route(_id, method=Method.DELETE.name, handler=delete_vehicle),
]
api_app: App = App(_routes, "templates", "static")


if __name__ == "__main__":
    setup: Setup = Setup()
    api_app.serve(setup.host, setup.port, setup.debug)
