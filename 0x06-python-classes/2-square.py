#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    define a class
    """
    def __init__(self, size=0):
        """
        initialize instance with optional size
        parameter

        size: must be an integer
        raise TypeError if not an integer
        """
        self.__size = size
        try:
            assert type(size) == int
        except:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
