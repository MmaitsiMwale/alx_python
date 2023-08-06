"""This is the base class that will be used to manage the attribute [id]"""


class Base:
    """Base Class to manage attribute [id]"""
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
