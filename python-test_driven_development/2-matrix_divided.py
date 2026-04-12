#!/usr/bin/python3
"""This module divides all elements of a matrix by a number."""

def matrix_divided(matrix, div):
    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round (num/2, 2))

    new_matrix.append(new_row)

    return new_matrix
