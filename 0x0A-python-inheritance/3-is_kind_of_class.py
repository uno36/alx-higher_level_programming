#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ function check if the obj is the same class or inherit from
    a_class
    Args:
        obj, the object
        a_class, the class
    Return:
        returns True if the object is an instance of, or if the object is
        an instance of a class that inherited from, the specified class;
        otherwise False.
    """
    return isinstance(obj, a_class)
