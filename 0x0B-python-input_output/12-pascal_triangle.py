#!/usr/bin/python3
def pascal_triangle(n):
    oL = []
    if n <= 0:
        return oL
    for i in range(n):
        iL = []
        for j in range(n):
            iL.append(2 ** i)
    return oL