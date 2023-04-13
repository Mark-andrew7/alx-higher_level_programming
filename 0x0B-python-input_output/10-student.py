#!/usr/bin/python3
"""
no modules imported
"""


class Student:
    """
    defining a class
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dict rep of student

        attrs: optional argument
        """
        if type(attrs) == list(str):
            return {k: getattr(self, k) for k in attrs}
        return self.__dict__
