#!/usr/bin/python3
"""
no modules imported
"""


def write_file(filename="", text=""):
    """
    writes a string to text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
