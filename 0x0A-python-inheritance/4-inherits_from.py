#!/usr/bin/python3
"""
no modules imported
"""


def inherits_from(obj, a_class):
    """
    returns a boolean value
    """
    if issubclass(type(obj), a_class):
        return True
    return False
