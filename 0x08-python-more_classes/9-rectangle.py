#!/usr/bin/python3
"""
no modules imported
"""


class Rectangle:
    """
    define a class rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialize parameters with optional instance
        width: private instance attribute
        height: private instance attribute
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """
        return new instance of rectangle
        """
        return Rectangle(size, size)

    @property
    def width(self):
        """
        retrieves private instance attribute
        """
        return self.__width

    @property
    def height(self):
        """
        retrieves private instance attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        sets private instance attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        sets private instance attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width * self.__height)

    def __str__(self):
        """
        print rectangle with character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        new_s = ""
        for x in range(self.__height):
            for j in range(self.__width):
                new_s += str(self.print_symbol)
            new_s += "\n"
        return new_s.rstrip()

    def __repr__(self):
        """
        return string representation of rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        delete instance of rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns biggest rect based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
