"""A class that defines a square with a default size of 0"""


class Square:
    """A class that defines a square with a default size of 0"""

    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
