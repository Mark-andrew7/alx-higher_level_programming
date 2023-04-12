#!/usr/bin/python3
"""
no modules imported
"""


def append_write(filename="", text=""):
    """
    appends a string at end of text file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
