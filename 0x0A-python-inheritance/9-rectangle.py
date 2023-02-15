#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import class"""


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """initialize the passing variables
        Args:
            width: the width
            height: the height
        Attributes:
            __width: width of rectangle
            __height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area
        Return:
            return the area
        """
        return self.__height * self.__width

    def __str__(self):
        """print rectangle description: [Rectangle] <width>/<height>
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
