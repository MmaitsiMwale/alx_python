"""Rectangle inherits from Base and builds on it
    width: width of rectangle
    height: height of rectangle
    x: left edge coordinate (default 0)
    y: right edge coordinate (default 0)
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base and builds on it
        takes width, height, x, y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the value of width"""
        return self.__width

    @width.setter
    def width(self, val):
        """sets the value of width"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0 or type is None:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @height.setter
    def height(self, val):
        """sets the value of height"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val < 0 or type is None:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, val):
        """sets the value of x"""
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, val):
        """sets the value of y"""
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val
