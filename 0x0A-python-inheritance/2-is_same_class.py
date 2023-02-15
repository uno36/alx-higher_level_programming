#!/usr/bin/python3
def is_same_class(obj, a_class):
    """function check if obj and a_class are exact
    the same object
    Args:
          obj: the object
          a_class: the class
    Return:
          returns True if the object is exactly an instance of the
          specified class ; otherwise False.
    """
    return type(obj) is a_class
