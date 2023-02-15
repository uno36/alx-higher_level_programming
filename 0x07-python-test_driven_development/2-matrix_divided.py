#!/usr/bin/python3
"""Module to divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ This is a functiion that divides all elements of a matrix.
    Args:
        matrix: the matrix that need to divide
        div: division
    Return:
        return the result
    """

    ErrorMeg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(ErrorMeg)
    if len(matrix) == 0:
        raise TypeError(ErrorMeg)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(ErrorMeg)
        if len(i) == 0:
            raise TypeError(ErrorMeg)
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError(ErrorMeg)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in y] for y in matrix]
