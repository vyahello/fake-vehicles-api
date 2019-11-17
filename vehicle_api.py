from api.app import api_app, Setup


def _run_vehicle_api(setup: Setup) -> None:
    """Runs vehicle REST API."""
    api_app.serve(setup.host, setup.port)


if __name__ == "__main__":
    _run_vehicle_api(Setup())