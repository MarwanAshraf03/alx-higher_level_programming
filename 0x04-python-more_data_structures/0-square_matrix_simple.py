#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        matrix_row = []
        for j in i:
            matrix_row.append(j**2)
        new_matrix.append(matrix_row)
    return new_matrix
