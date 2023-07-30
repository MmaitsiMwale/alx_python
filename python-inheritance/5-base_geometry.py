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
        try:
            isinstance(value, int) and type(value) == int
        except:
            raise TypeError(f"{name} must be an integer")
        try:
            value > 0
        except:
            raise ValueError(f"{name} must be greater than 0")
