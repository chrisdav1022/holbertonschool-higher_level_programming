#!/usr/bin/python3
"""MyList"""


class MyList(list):
    """Class"""
    def print_sorted(self):
        """Print the list"""
        print(sorted(self))
