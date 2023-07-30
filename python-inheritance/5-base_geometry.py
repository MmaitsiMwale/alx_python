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
