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
        fileName = cls.__name__ + '.json'
        with open(fileName, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_objs = [y.to_dictionary() for y in list_objs]
                string = cls.to_json_string(list_objs)
                f.write(string)

    def from_json_string(json_string):
        """
        return list of JSON string rep
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ = Rectangle:
            r1 = Rectangle(4, 6)
        elif cls.__name__ = Square:
            r1 = Square(7)

        r1.update(**dictionary)
        return r1
