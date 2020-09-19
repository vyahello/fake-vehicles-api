from api.app import api_app
from api.setup import Setup


def __main(setup: Setup) -> None:
    """Runs vehicle REST API."""
    api_app.serve(setup.host, setup.port)


if __name__ == "__main__":
    __main(Setup())
