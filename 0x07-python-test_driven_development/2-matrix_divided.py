#!/usr/bin/python3
def matrix_divided(matrix, div):

    if ((type(matrix) is not list) or
        (not all(type(row) is list for row in matrix)) or
            (not all(
            type(i) in (float, int) for row in matrix for i in row))):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for i, ls in enumerate(matrix):
        if len(ls) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (float, int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in y] for y in matrix]
