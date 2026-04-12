#!/usr/bin/python3
"""Divides all elements of a matrix by div and returns a new matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix."""

    if matrix == [] or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # compute result
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix
