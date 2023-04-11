#!/usr/bin/python3
"""
no modules imported
"""


def is_kind_of_class(obj, a_class):
    """
    checks instance of object or
    class inherited from
    """
    if isinstance(obj, a_class):
        return True
    if issubclass(type(obj), a_class):
        return False
    return False
