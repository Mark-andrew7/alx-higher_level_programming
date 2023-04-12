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

    def to_json(self):
        """
        retrieves dictionary representation
        """
        return self.__dict__
