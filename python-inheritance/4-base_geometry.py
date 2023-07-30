"""
Geometry Class based on 3-base_geometry with non defined
method area()
"""


class BaseGeometry(BaseGeometry):
    """Geometry Class"""

    def __init__(self):
        super().__init__()

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")
