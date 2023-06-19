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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string rep
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.height)

    @property
    def size(self):
        """
        getter method
        """
        return self.size

    @size.setter
    def size(self, value):
        """
        setter method
        """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        return dictionary rep
        """
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
