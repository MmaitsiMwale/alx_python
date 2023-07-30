"""
Geometry Class based on 3-base_geometry with non defined
method area().
"""


class BaseGeometry:
    """
    Geometry Class with undefined area() method
    """

    def area(self):
        """raise exception that area is not defined"""
        raise Exception("area() is not implemented")
