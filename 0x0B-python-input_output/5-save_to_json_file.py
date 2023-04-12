#!/usr/bin/python3
"""
imports json module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes object to text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
