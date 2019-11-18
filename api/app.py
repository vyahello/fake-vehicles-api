from apistar import App, Route
from api.routes import list_vehicles, create_vehicle
from dataclasses import dataclass
from api.web.support import Method

_root: str = "/"


@dataclass(frozen=True)
class Setup:
    """The class represents application setup."""

    host: str = "0.0.0.0"
    port: int = 5000
    debug: bool = False


api_app: App = App(
    [
        Route(_root, method=Method.GET.name, handler=list_vehicles),
        Route(_root, method=Method.POST.name, handler=create_vehicle),
    ]
)
