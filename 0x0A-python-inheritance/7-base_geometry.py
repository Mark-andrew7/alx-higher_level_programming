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
            raise TypeError("<name> must be an integer")
        elif value < 0 or == 0:
            raise ValueError("<name> must be greater than 0")
