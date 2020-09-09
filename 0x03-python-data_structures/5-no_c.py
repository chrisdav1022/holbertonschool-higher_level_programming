#!/usr/bin/python3
def no_c(my_string):
    ec = ""
    for n in my_string:
        if n != 'c' and n != 'C':
            ec += n
    return ec
