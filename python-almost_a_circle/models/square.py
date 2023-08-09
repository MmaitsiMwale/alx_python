"""Square class inherits from Rectangle Class
    size: size of square sides
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle Class
    size: size of square sides
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self) -> str:
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, val):
        """sets size of square"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0 or type is None:
            raise ValueError("width must be > 0")
        self.__size = val
