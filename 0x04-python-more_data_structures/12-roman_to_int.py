#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return None
    s = 0
    nroman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
              'D': 500, 'M': 1000}

    for i in range(len(roman_string)):
        check = 0
        num = nroman.get(roman_string[i])
        if num is None:
            return 0
        if i < len(roman_string) - 1:
            check = nroman.get(roman_string[i + 1])
        s += num if num >= check else - num
    return s
