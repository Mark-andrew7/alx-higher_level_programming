#!/usr/bin/python3
"""
inheritance
"""


class Base:
    """
    define a class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
