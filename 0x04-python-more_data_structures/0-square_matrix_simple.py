#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = list(map(list, matrix))
    for i in new:
        for j in range(0, len(i)):
            i[j] = i[j]**2
    return new
