def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix."""

    # ❗ 1. check empty FIRST (very important)
    if matrix == [] or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # ❗ 2. check structure
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # ❗ 3. ONLY NOW safe to use matrix[0]
    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
