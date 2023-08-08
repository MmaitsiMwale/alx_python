"""This is the base class that will be used to manage the attribute [id]"""


class Base:
    """Base Class to manage attribute [id]"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
