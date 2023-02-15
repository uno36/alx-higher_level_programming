#!/usr/bin/python3
def inherits_from(obj, a_class):
    """determine if the object is the only sub class a_class
    Args:
        obj: the object
        a_class: the class
    Return:
        returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class;
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
