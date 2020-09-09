#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        n = my_list
        for i in my_list:
            if i > n:
                n = i
    return i
