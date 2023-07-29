"""
function that returns True if the object is exactly an instance of the
specified class ; otherwise False. 
"""


def is_same_class(obj, a_class):
    """Return True if obj belongs to the same class as `a_class`."""
    return isinstance(obj, a_class) and type(obj) == a_class
