#!/usr/bin/python3
"""
no modules imported
"""


def class_to_json(obj):
    """
    returns dictionary description with
    simple data structure list
    """
    return obj.__dict__
