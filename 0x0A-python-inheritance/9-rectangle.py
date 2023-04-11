#!/usr/bin/python3
"""
no modules imported
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle class that inherits
    from basegeometry
    """
    def __init__(self, width, height):
        """
        initialization
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        implementation of area method
        """
        self.__width * self__height

    def __str__(self):
        """
        return rectangle description
        """
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
