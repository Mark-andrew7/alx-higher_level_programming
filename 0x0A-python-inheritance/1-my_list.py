#!/usr/bin/python3
"""
no modules imported
"""


class MyList(list):
    """
    define a class that inherits
    """
    def print_sorted(self):
        """
        prints a sorted list
        """
        print(sorted(self))
