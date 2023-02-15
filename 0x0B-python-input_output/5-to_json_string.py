#!/usr/bin/python3
def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    Args:
        my_obj: the string object that need to serialize to a JSON formatted
    Return:
        return the serialized object
    """
    import json
    return json.dumps(my_obj)
