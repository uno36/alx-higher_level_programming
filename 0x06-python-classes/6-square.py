#!/usr/bin/python3
"""My Square module"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a square
        Args:
            size: length of a side
            position: the (x, y) displacement of the square from the left
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property getter for size"""
        return self.__size

    @property
    def position(self):
        """Property getter for position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Property setter for size
        Args:
            value: length of a side
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Property setter for position
        Args:
            value: a tuple of 2 positive integers defining x and y offset
        Raises:
            TypeError: if value is not a tuple with 2 elements
        """
        if isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculate the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square using #"""
        if self.__size == 0:
            print()

        xOffset = self.__position[0]
        yOffset = self.__position[1]

        while yOffset > 0:
            print()
            yOffset -= 1

        y = self.__size
        while y > 0:
            x = self.__size
            xOffset = self.__position[0]
            while xOffset > 0:
                print(" ", end="")
                xOffset -= 1
            while x > 0:
                print("#", end="\n" if x == 1 else "")
                x -= 1
            y -= 1
