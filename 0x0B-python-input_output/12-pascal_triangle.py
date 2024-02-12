#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """
    Pascal's triangle function

    Args:
    n: number of rows

    Return:
    returns list of lists
    that represents a pascal's
    triangle
    """
    oL = []
    if n <= 0:
        return oL
    for i in range(n):
        iL = []
        for j in range(n):
            iL.append(2 ** i)
    return oL
