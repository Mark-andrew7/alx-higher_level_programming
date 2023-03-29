#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    defines square with private instance attribute
    """
    def __init__(self, size=0):
        """
        initialize an optional instance size

        size: private instant attribute
        """
        self.__size = size

    @property
    def size(self):
        """
        method that retrieves private instant attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method that sets private instant attribute
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdoutput square with character #
        """
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
