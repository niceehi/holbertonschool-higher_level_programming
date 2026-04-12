#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round (num/2, 2))

    new_matrix.append(new_row)

    return new_matrix
