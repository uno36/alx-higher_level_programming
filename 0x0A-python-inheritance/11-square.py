#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """initialize the passing variables
        Args:
            size: size of square
        Attributes:
           __size: size of square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculate the area of square
        Return:
           return the area of square
        """
        return self.__size**2

    def __str__(self):
        """print square description
        Return:
            return square description
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
