#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(i):
            print()
        for j in range(len(i)):
            print("{:d}".format(
                i[j]), end=" " if
                 j < len(matrix[i]) else "")
        print()
