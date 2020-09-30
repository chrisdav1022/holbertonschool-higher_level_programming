#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the data width and the height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Print the rectangle with the '#'"""
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        string += ((str(self.print_symbol) * self.__width + '\n') *
                   self.__height)
        return string[:-1]

    def __repr__(self):
        """String representation of the rectangle"""
        return ('Rectangle(' + str(self.__width) + ', ' +
                str(self.__height) + ')')

    def __del__(self):
        """Delete the rectangle"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width for the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height for the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Get the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Ger the biggest rectangle based on the area"""
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
