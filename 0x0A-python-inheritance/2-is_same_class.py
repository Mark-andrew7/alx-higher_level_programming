#!/usr/bin/python3
"""
no modules imported
"""


def is_same_class(obj, a_class):
    """
    function that returns a boolean value
    """
    if isinstance(type(obj), a_class):
        return True
    return False
