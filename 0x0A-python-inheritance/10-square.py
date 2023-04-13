#!/usr/bin/python3
"""
inheritance
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square that inherits
    from rectangle
    """
    def __init__(self, size):
        """
        initialization
        """
        super().__init__(self, self)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        implementation of area
        """
        return self.__width * self.__height
