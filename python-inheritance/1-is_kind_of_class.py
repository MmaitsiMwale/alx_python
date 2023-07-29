"""
a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """return True if object is instance or subclass of a class"""
    return issubclass(type(obj), a_class)
