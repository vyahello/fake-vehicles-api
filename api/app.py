from apistar import App, Route
from api.routes import list_vehicles
from dataclasses import dataclass


@dataclass(frozen=True)
class Setup:
    """The class represents application setup."""
    host: str = "0.0.0.0"
    port: int = 5000
    debug: bool = False


api_app: App = App([Route("/", method="GET", handler=list_vehicles)])
