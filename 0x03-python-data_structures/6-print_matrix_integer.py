#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        i = 0
        for j in arr:
            if i < len(arr) - 1:
                print("{:d}".format(j), end='')
            else:
                i = i + 1
        print("")
