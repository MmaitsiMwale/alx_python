#!/usr/bin/python3
"""A class that defines a square with a default size of 0
    methods: area()
"""


class Square:
    """A class that defines a square with a default size of 0
        methods: area()
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Returns the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square object of size = size"""
        return self.__size ** 2
