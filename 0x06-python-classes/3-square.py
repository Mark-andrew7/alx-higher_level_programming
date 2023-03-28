#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    define a class
    """
    def __init__(self, size)
    """
    initializes an optional instance size

    size: must be an integer
    otherwise raise a TypeError
    """
    self.__size = size
    try:
        type(size) == int
    except:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    def area(self):
        """
        public instance method
        returns current square area
        """
        return self.__size ** 2
