#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for m in matrix:
        new_row = []
        for i in m:
            new_row.append(i * i)
        new_matrix.append(new_row)
    return new_matrix
