#!/usr/bin/python3
"""
inheritance
"""
from models.base import Base


class Rectangle(Base):
    """
    inheritance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        gettter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        setter method
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle instance using # character"""
        for i in range(self.__y):
            print()
        for n in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for m in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        method that assigns attributes
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

        try:
            if args:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.width = args[1]
                if len(args) >= 3:
                    self.height = args[2]
                if len(args) >= 4:
                    self.x = args[3]
                if len(args) >= 5:
                    self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        """Str method to returns rectangle representation"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def to_dictionary(self):
        """
        returns dictionary rep
        """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
