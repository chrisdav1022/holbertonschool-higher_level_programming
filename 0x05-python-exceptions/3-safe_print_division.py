#!/usr/bin/python3
def safe_print_division(a, b):
    i = None
    try:
        i = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(i))
        return i
