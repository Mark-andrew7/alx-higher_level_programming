#!/usr/bin/python3
"""
import the json module
"""
import json


def from_json_string(my_str):
    """
    return object rep by JSON str
    """
    return json.loads(my_str)
