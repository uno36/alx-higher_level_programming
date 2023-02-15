#!/usr/bin/python3
def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
       filename: name of the file
    Return:
       return the deserialized object
    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
