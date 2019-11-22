from apistar import Route, App
from api.app import ROUTES, api_app


def test_count_routes() -> None:
    assert len(ROUTES) == 6


def test_first_route_type() -> None:
    assert isinstance(ROUTES[0], Route)


def test_last_route_type() -> None:
    assert isinstance(ROUTES[-1], Route)


def test_app() -> None:
    assert isinstance(api_app, App)
