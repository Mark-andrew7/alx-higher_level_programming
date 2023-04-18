#!/usr/bin/python3
"""
inheritance
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    inheritance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization
        """
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """
        string rep
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)
