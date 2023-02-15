#!/usr/bin/python3
def append_write(filename="", text=""):
    """appends a string at the end of a text file
    Args:
       filename: name of the file
       text: text of the file
    Return:
       number of characters added
    """
    with open(filename, "a") as f:
        return f.write(text)
