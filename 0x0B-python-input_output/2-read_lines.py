#!/usr/bin/python3
"""read to number lines"""


def read_lines(filename="", nb_lines=0):
    """read the file"""
    with open(filename, 'r') as fl:
        if nb_lines <= 0:
            print(fl.read(), end='')
            return
        c = 0
        for line in fl:
            if c < nb_lines:
                print(line, end='')
            c += 1
