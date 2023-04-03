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
