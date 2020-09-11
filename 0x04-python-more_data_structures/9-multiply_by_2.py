#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newn = {}
    for key in a_dictionary:
        i = a_dictionary[key] * 2
        newn[key] = i
    return newn
