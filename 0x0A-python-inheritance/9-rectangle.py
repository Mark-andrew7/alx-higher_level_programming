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
        return self.__width * self__height

    def __str__(self):
        """
        return rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
