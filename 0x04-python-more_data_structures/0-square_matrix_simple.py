#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[matrix[i][j]**2 for j in range(len(matrix[0]))]
            for i in range(len(matrix))]
