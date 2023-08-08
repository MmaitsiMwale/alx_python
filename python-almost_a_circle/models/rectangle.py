"""Rectangle inherits from Base and builds on it
    width: width of rectangle
    height: height of rectangle
    x: left edge coordinate (default 0)
    y: right edge coordinate (default 0)
"""

Base = __import__('base.py').Base


class Rectangle(Base):
    """Rectangle inherits from Base and builds on it
        takes width, height, x, y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__()
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
        self.__width = val

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @height.setter
    def height(self, val):
        """sets the value of height"""
        self.__height = val

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, val):
        """sets the value of x"""
        self.__x = val

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, val):
        """sets the value of y"""
        self.__y = val
