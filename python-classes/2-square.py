"""A class that defines a square with a default size of 0
    methods: area()
"""


class Square:
    """A class that defines a square with a default size of 0
        methods: area()
    """

    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of a square object of size = size"""

        return self.__size ** 2
