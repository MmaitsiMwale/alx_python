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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the object"""
        return f"[Rectangle] {self.__width}/{self.__height})"
