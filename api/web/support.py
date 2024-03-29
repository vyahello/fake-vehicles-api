"""The module contains API to HTTP WEB support."""
from enum import Enum
from apistar.http import JSONResponse


class Status(Enum):
    """The class represents enumeration of HTTP statuses."""

    SUCCESS: int = 200
    CREATED: int = 201
    NO_CONTENT: int = 204
    NOT_FOUND: int = 404

    @property
    def code(self) -> int:
        return self.value


class Method(Enum):
    """The class represents enumeration of HTTP methods."""

    GET: str = "get"
    POST: str = "post"
    PUT: str = "put"
    DELETE: str = "delete"


RESPONSE_ERROR = JSONResponse(content={"error": "vehicle not found"}, status_code=Status.NOT_FOUND.code)
