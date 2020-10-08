#!/usr/bin/python3
"""Function that append"""


def append_write(filename="", text=""):
    """string to a file"""
    with open(filename, 'a') as fl:
        return fl.write(str(text))
