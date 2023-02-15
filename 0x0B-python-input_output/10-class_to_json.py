#!/usr/bin/python3
def class_to_json(obj):
    """ serialize an obj class
    Args:
        obj: the object that need to serialize
    Return:
        return the serialized object
    """
    return obj.__dict__
