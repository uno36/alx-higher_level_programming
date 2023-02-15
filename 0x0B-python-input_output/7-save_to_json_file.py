#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj: the object that need to serialize to JSON formatted str
        filename: name of the file
    """
    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
