#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    defines a class
    """
    def __init__(self, size=0):
        """
        initializes an optional instance size

        size: private instance attribute
        """
    @property
    def size(self):
        """
        method that retrieves attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method that sets attribute
        """
        self.__size = value
    try:
        type(size) == int
    except TypeError:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    def area(self):
        """
        public instance method
        returns current square area
        """
        return self.__size ** 2
