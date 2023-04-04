#!/usr/bin/python3
"""
no modules imported
"""


class Rectangle:
    """
    define a class rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initialize parameters with optional instance
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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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
        return 2 * (self.__width * self.__height)

    def __str__(self):
        """
        print rectangle with character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        new_s = ""
        for x in range(self.__height):
            for j in range(self.__weight):
                new_s += "#"
            new_s += "\n"
        return new_s.rstrip

    def __repr__(self):
        """
        return string representation of rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
