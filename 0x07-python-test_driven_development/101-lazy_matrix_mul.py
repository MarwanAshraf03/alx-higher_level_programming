#!/usr/bin/python3
import numpy as numpy
def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul - multiplies two matrices using the module NumPy.

    Args:
        m_a: The first matrix
        m_b: The second matrix

    Returns:
        A new matrix
    """
    return (numpy.matmul(m_a, m_b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
