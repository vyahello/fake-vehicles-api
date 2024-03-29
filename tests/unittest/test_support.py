import pytest
from api.web.support import Status, Method
from tests.markers import unittest


@unittest
def test_status() -> None:
    assert isinstance(Status.CREATED, Status)


@unittest
@pytest.mark.parametrize("status, code", [(Status.SUCCESS, 200), (Status.CREATED, 201), (Status.NOT_FOUND, 404)])
def test_status_code(status: Status, code: int) -> None:
    assert Status.CREATED.code == 201


@unittest
@pytest.mark.parametrize("method", [Method.GET, Method.POST, Method.PUT])
def test_method(method: Method) -> None:
    assert isinstance(method, Method)


@unittest
@pytest.mark.parametrize("method, value", ((Method.GET, "get"), (Method.POST, "post")))
def test_method_value(method: Method, value: str) -> None:
    assert method.value == value
