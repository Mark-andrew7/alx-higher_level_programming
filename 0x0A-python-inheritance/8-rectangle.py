#!/usr/bin/python3
"""
no modules imported
"""


class BaseGeometry:
    """
    defining a class
    """
    def area(self):
        """
        public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method that
        validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class inheritance
    """
    def __init__(self, width, height):
        """
        initialization
        """
        self.integer_validator("width", width)
        self.integer_validator("height", width)
        self.__width = width
        self.__height = height
