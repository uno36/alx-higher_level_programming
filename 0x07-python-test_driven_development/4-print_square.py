#!/usr/bin/python3
"""Module to prints square
"""


def print_square(size):
    """ This function prints square
    Args:
        size: the size of square
    """

    if size is None:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format('#' * size))
