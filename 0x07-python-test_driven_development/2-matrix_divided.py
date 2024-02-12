#!/usr/bin/python3
"""Matrix Division Module"""


def matrix_divided(matrix, div):
    """
    Divides matrix elements with div

    Args:
    matrix: matrix to be used
    div: number to be divided by

    Return: returns new matrix consists
            of divided elements of matrix
    """

    if type(div).__name__ not in ("int", "float"):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    s = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(s)
    if len(matrix) == 0:
        raise TypeError(s)
    if not isinstance(matrix[0], list):
        raise TypeError(s)
    if len(matrix[0]) == 0:
        raise TypeError(s)
    if not all([isinstance(i, list) for i in matrix]):
        raise TypeError(s)
    if not all([isinstance(k, (int, float)) for i in matrix for k in i]):
        raise TypeError(s)
    if not all([len(j) == len(matrix[0]) for j in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    mat_size = (len(matrix), len(matrix[0]))
    ret = []
    for counter in range(mat_size[0]):
        inner = []
        for counter2 in range(mat_size[1]):
            inner.append(round((matrix[counter][counter2])/div, 2))
        ret.append(inner)
    return ret


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
