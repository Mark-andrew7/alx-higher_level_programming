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
        """
        self.__size = size

    try:
        size == integer
    except TypeError:
        print("size must be an integer")
    if size < 0:
        raise ValueError:
            print("size must be >= 0")
