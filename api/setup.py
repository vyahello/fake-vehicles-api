from dataclasses import dataclass
from typing import NamedTuple


@dataclass(frozen=True)
class _Directory:
    """The class represents application directory setup."""

    templates: str = "templates"
    static: str = "static"


@dataclass(frozen=True)
class Setup:
    """The class represents application setup."""

    host: str = "0.0.0.0"
    port: int = 5000
    debug: bool = False
    dir_: _Directory = _Directory()


class MoveTo(NamedTuple):
    """The class represents holder for redirect route on action."""

    root: str = "/rest"
    index: str = "/index.html"
    id_: str = "/rest/{vehicle_id}"
