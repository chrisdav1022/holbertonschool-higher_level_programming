#!/usr/bin/python3
"""Geometry Class"""


class BaseGeometry:
    """Geometry"""

    def area(self):
        """Raise exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits"""

    def __init__(self, width, height):
        """Rectangle parameters"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __repr__(self):
        """Return the width and height"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """Return the area"""
        return self.__width * self.__height
