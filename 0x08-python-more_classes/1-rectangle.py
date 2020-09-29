#!/usr/bin/python3
"""init python3"""


class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the data."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """save width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """save height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
