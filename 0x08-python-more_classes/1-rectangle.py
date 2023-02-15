#!/usr/bin/python3
class Rectangle:
    """This is a class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """This is a function that use __init__ method to
        initialize the passing variables
        Args:
             width: width of rectangle
             height: height if rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter: get width of rectangle
        Return:
              return the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: set the argument value to width
        Attributes:
              ___width: width of rectangle
        Args:
              value: width of rectangle
        Raises:
              TypeError: width must be an integer
              ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: get height of rectangle
        Return:
             return the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: set the argumet value to height
        Attributes:
               __height: the height of rectangle
        Args:
               value: the height of rectangle
        Raises:
               TypeError: height must be an integer
               ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
