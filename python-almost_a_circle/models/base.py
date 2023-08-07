"""This is the base class that will be used to manage the attribute [id]"""


class Base:
    """Base Class to manage attribute [id]"""
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            self.id = id
        else:
            new_id = __class__.__nb_objects + 1
            self.id = new_id

    # @id
    # def id():
    #     """get the id passed to the function"""
    #     pass

    # @property
    # def id():
    #     """set the id with condition"""
    #     pass
