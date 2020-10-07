#!/usr/bin/python3
"""read number lines"""


def read_lines(filename="", nb_lines=0):
    """Function reads file"""
    with open(filename, 'r') as fl:
        if nb_lines <= 0:
            print(fl.read(), end='')
            return
        ct = 0
        for line in fl:
            if ct < nb_lines:
                print(line, end='')
            ct += 1
