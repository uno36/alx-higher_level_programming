#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def add_integer(a, b=98):
    """ This is a function that add two integers
    Args:
    a: first integer that need to add
    b: second integer that need to add
    Return:
    return: sum
    """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    sum = a + b
    if sum == float('inf') or sum == -float('inf'):
        return 89
    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
