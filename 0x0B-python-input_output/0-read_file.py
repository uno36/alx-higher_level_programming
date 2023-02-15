#!/usr/bin/python3
def read_file(filename=""):
    """read a file and print full content of the file
    Args:
        filename: the name of the file
    """
    with open(filename) as f:
        data = f.read()
    print("{}".format(data), end="")
