#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    define a class with private instance attribute
    """
    def __init__(self, size=0):
        """
        initializes an optional instance size

        size: must be an integer
        otherwise raise a TypeError
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        public instance method
        returns current square area
        """
        return self.__size ** 2
