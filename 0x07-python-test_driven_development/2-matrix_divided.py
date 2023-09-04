#!/usr/bin/python3
def matrix_divided(mat, div):
    mat_bool = any(isinstance(i, list) for i in mat)
    if type(div).__name__ not in ("int", "float"):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(mat, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(mat) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(mat[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    len_check = all([len(i) == len(mat[0]) for i in mat])
    if not len_check:
        raise TypeError("Each row of the matrix must have the same size")
    mat_size = (len(mat), len(mat[0]))
    ret = []
    for counter in range(mat_size[0]):
        inner = []
        for counter2 in range(mat_size[1]):
            num = mat[counter][counter2]
            if type(num).__name__ not in ("int", "float"):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            inner.append(round((mat[counter][counter2])/div, 2))
        ret.append(inner)
    return ret
