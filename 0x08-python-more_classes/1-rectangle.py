#!/usr/bin/python3
"""
no modules imported
"""


class Rectangle:
    """
    class that defines an __init__ method
    """
    def __init__(self, width=0, height=0):
        """
        initializes parameter with optional instance

        width: private instance attribute
        height: private instance attribute
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves a private instance attribute
        """
        return self.__width

    @property
    def height(self):
        """
        retrieves a private instance attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        sets a private instance attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        sets a private instance attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
