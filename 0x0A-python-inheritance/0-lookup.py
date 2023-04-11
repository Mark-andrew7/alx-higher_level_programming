#!/usr/bin/python3
"""
no modules imported
"""


def lookup(obj):
    """
    returns list of available attributes
    """
    for i in obj:
        return dir(i)
