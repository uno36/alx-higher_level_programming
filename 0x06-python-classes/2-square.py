#!/usr/bin/python3
class Square:
    """this is a class Square that defines a square
    Attributes:
       __size: Private instance attribute - size of square
    Args:
       size: size of square.
    """
    def __init__(self, size=0):
        """This is a function that use __init__ method to
        initialize the passing variables

        Attributes:
             __size: Private instance attribute - size of square
        Args:
             size: size of square
        Raises:
             TypeError: size must be an integer
             ValueError: size must be >= 0
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
