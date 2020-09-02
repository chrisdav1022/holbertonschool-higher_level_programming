#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastt = number % -10
        lastt = -lastt
    else:
        lastt = number % 10
    print("{:d}".format(lastt), end="")
    return(lastt)
