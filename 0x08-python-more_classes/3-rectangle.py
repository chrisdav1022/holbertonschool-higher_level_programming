#!/usr/bin/python3
"""init rectangle"""


class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the data."""
        self.width = width
        self.height = height

    def __str__(self):
        """Print rectangle"""
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        string += ('#' * self.__width + '\n') * self.__height
        return string[:-1]

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
