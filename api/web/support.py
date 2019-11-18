"""The module contains API to HTTP WEB support."""
from enum import Enum


class Status(Enum):
    """The class represents enumeration of HTTP statuses."""

    SUCCESS: int = 200
    CREATED: int = 201

    @property
    def code(self) -> int:
        return self.value


class Method(Enum):
    """The class represents enumeration of HTTP methods."""

    GET: str = "get"
    POST: str = "post"
