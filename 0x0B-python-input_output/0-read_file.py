#!/usr/bin/python3
"""
no modules imported
"""


def read_file(filename=""):
    """
    reads a text file
    """
    with open(filename, "r", encoding="utf-8") as f:
        for readline in f:
            print(readline, end="")
