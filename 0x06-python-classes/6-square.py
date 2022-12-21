#!/usr/bin/python3
class Square:
    """Class of the square"""
    def __init__(self, size=0, position=(0, 0)): 
        """Init self"""
        self.__size = size
        """Orientation of square"""
        self.position = position
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        """Conditions"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Current square area"""
        return self.__size ** 2
    def my_print(self):
        if self.__size is 0:
            print ()
        else:
            print('\n' * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value



    """def size(self):
        return self.__size"""
