#!/usr/bin/python3
"""0-add_integer module"""

def add_integer(a, b=98):
    """Add two integers
    Args:
        a: the first number
        b: the second number. Defaults to 98
    Raises:
        TypeError: if a or b is not an integer
    """

    if type(a) not in (float, int):
        raise TypeError('a must be an integer')

    if type(b) not in (float, int):
        raise TypeError('b must be an integer')

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
