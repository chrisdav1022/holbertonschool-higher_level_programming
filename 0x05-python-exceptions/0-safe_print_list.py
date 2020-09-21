#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        p1 = 0
        while p1 < x:
            print(my_list[p1], end='')
            p1 += 1
        print()
    except:
        print()
    return p1
