#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New = []
    for i in matrix:
        New.append(list(map(lambda i: i ** 2, i)))
    return New
