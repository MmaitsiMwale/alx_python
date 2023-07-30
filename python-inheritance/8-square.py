"""
Class Square that inherits from Rectangle
"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Square class with properties and methods for calculating area,
    perimeter etc."""

    def __init__(self, size):
        """Square constructor recieves 1 size integers"""
        super().__init__(size, size)
        self.integer_validator("width", size)
        self.__size = size

    def area(self):
        """return area of square"""
        return self.__size ** 2
