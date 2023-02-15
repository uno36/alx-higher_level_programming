#!/usr/bin/python3
def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the
    number of characters written.
    Args:
        filename: name of the file
        text: text of the file
    Return:
        number of characters written
    """
    with open(filename, "w") as f:
        return f.write(text)
