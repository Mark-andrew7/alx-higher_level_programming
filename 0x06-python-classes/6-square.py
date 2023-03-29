#!/usr/bin/python3
"""
no modules imported
"""


class Square:
    """
    defines a square with private instance attributr
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializes optional instance size and position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        method to retrieve private instance attribute
        """
        return self.__size = size

    @property
    def position(self):
        """
        method to retrieve private instance attribute
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        method that sets private instance attribute
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        method that sets private instance attribute
        """
        if not isinstance(value, tuple) or
        len(value) != 2 or
        not all(isinstance(y, int) for y in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        returns current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with character #
        """
        if size == 0:
            print()
        for i in range(self.__position[1]):
            print("\n")
        for i in range(self.__size):
            for j in range(self.__position[0]:
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
