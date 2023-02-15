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
        self.size = size

    @property
    def size(self):
        """Getter: get size of square
        Return:
           return the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: set the argument value to size
        Attributes:
             __size: Private instance attribute - size of square
        Args:
             size: size of square
        Raises:
             TypeError: size must be an integer
             ValueError: size must be >= 0
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        return self.__size

    def area(self):
        """ This is a function calculate the area of a square
        Attributes:
             __size: Private instance attribute - size of square
        Returns:
             the result
        """
        return self.__size ** 2
