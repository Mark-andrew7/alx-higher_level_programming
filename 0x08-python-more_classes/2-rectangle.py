#!/usr/bin/python3
"""
no modules imported
"""


class Rectangle:
    """
    defines a class rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initializes parameters with optional instance

        width: private instance attribute
        height: private instance attribute
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        retrieves private instance attribute
        """
        return self.__width

    @property
    def height(self):
        """
        retrieves private instance attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        sets private instance attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        sets private instance attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
