#!/usr/bin/python3
"""
inheritance
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        dictionary to JSON string
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
