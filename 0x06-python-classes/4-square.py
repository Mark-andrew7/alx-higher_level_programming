#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    defines a square with private instant attribute
    """
    def __init__(self, size=0):
        """
        initializes an optional instance size

        size: private instance attribute
        """
        self.__size = size

    @property
    def size(self):
        """
        method that retrieves a private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method that sets a private attribute
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        public instance method
        returns current square area
        """
        return self.__size ** 2
