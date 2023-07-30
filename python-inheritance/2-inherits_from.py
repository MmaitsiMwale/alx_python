"""
Function that returns True if the object is an instance of a
class thatinherited (directly or indirectly) from the specified
class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """returns True if the object obj is an instance of a
    class that inherits"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
