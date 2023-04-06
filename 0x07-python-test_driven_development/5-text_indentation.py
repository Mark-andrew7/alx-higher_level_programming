#!/usr/bin/python3
"""
no modules imported
"""


def text_indentation(text):
    """
    prints a text with two new lines
    after '.', '?', ':'
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    
