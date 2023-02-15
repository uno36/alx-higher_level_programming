#!/usr/bin/python3
def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string
    Args:
        my_str: the string that need to deserialize to a python object
    Return:
        return the deserialized object
    """
    import json
    return json.loads(my_str)
