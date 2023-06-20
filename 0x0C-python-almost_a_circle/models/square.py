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
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        return dictionary rep
        """
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
