#!/usr/bin/python3
"""Define a Base class"""

from os import path
import json
import csv


class Base:
    """Define a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
