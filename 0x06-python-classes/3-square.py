#!/usr/bin/python3
"""My Square module"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Define the size of the square
        Args:
            size: length of a side
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
