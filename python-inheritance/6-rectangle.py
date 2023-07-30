"""
Class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with properties and methods for calculating area,
    perimeter etc."""

    def __init__(self, width, height):
        """Rectangle constructor recieves +ve integers"""
        super().__init__()
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height
