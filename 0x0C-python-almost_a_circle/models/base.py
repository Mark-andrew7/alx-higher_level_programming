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
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string to file
        """
        fileName = class.__name__ + 'json'
        with open(fileName, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_objs = [y.to_dictionary() for y in list_objs]
                string = cls.to_json_string(list_objs)
                f.write(string)
