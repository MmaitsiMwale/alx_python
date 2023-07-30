"""
Geometry Class based on 4-base_geometry with method
integer_validator to validate an integer.
"""


class BaseGeometry:
    """
    Geometry Class with undefined area() method
    """

    def area(self):
        """raise exception that area is not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""
        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
