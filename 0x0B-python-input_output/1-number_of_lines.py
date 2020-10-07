#!/usr/bin/python3
"""read number lines"""


def number_of_lines(filename=""):
    """c count the number of lines"""
    c = 0
    with open(filename, 'r') as f:
        for line in f:
            c += 1
    return c
