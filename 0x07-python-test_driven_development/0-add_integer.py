#!/usr/bin/python3
"""
no modules imported
"""


def add_integer(a, b=98):
    """
    adds two integers together and returns an int value
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
