#!/usr/bin/python3
"""Lazy Matrix Multiplication Module"""
import numpy as numpy


def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul - multiplies two matrices using NumPy.

    Args:
        m_a: first matrix
        m_b: second matrix

    Return:
        returns a matrix with multiplication of m_a and m_b
    """
    return (numpy.matmul(m_a, m_b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
