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

        """
        self.__size = size

    try:
        assert type(size) == int
    except TypeError:
        print("size must be an integer")
    if size < 0:
        raise ValueError:
            print("size must be >= 0")
