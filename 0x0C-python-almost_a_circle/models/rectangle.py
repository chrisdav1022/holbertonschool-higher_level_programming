#!/usr/bin/python3
"""Define a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Define a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        def __str__(self):
            """Print the rectangle attributes."""
            return ('[Rectangle] (' + str(self.id) + ') ' + str(self.__x) + '/' +
                    str(self.__y) + ' - ' + str(self.__width) + '/' +
                    str(self.__height))
