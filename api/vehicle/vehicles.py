from apistar.types import Type
from apistar.validators import Integer, String
from api import LIST_OF_MANUFACTURERS


class Vehicle(Type):
    """The class represents a single vehicle.

    Please be aware that it contains data type validation under the hood (from `Type` class).
    """

    id_: Integer = Integer(allow_null=True)
    manufacturer: String = String(max_length=30, enum=LIST_OF_MANUFACTURERS)
    model: String = String(max_length=30)
    year: Integer = Integer(minimum=1900, maximum=2050)
    vin: String = String(max_length=50, default="")
