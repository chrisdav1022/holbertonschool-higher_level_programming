#!/usr/bin/python3
"""python"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the data"""
        self.size = size

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """the area of the square"""
        return self.__size**2
