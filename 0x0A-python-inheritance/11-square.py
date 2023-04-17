#!/usr/bin/python3
"""
inheritance
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    defines a class square
    """
    def __init__(self, size):
        """
        initialization
        """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        return square description
        """
        return "[square] {}/{}".format(self.__size, self.__size)
