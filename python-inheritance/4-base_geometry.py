"""
Geometry Class BaseGeometry
"""


class BaseGeometry(BaseGeometry):
    """Geometry Class"""

    def __init__(self):
        super().__init__()

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")
