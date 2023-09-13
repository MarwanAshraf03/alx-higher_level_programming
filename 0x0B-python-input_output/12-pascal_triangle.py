#!/usr/bin/python3
def pascal_triangle(n):
    oL = []
    if n <= 0:
        return oL
    for i in range(1, n+1):
        iL = []
        for j in range(i+1):
            iL.append(j)
        oL.append(iL)
    return oL