#!/usr/bin/python3
"""Matrix Multiplication Module"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matricies

    Args:
    m_a: first matrix (list of lists of integer and float numbers)
    m_b: second matrix (list of lists of integer and float numbers)

    Return:
    returns: new matrix which is the product of m_a and m_b
    """

    # check if matrix is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    # check if matrix is list of lists
    if not all([isinstance(i, list) for i in m_a]):
        raise TypeError("m_a must be a list of lists")
    if not all([isinstance(i, list) for i in m_b]):
        raise TypeError("m_b must be a list of lists")
    # check if matrices are empty
    if (len(m_a) == 0):
        raise ValueError("m_a can't be empty")
    if (len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if (len(m_b) == 0):
        raise ValueError("m_b can't be empty")
    if (len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    # check if values are not int or float
    if not all([isinstance(k, (int, float)) for i in m_a for k in i]):
        raise TypeError("m_a should contain only integers or floats")
    if not all([isinstance(k, (int, float)) for i in m_b for k in i]):
        raise TypeError("m_b should contain only integers or floats")
    # check that each row is of the same length
    if not all([len(j) == len(m_a[0]) for j in m_a]):
        raise TypeError("each row of m_a must be of the same size")
    if not all([len(j) == len(m_b[0]) for j in m_b]):
        raise TypeError("each row of m_b must be of the same size")
    m_a_dim = (len(m_a), len(m_a[0]))
    m_b_dim = (len(m_b), len(m_b[0]))
    # check if dimensions are able to be multiplied
    if not (m_a_dim[1] == m_b_dim[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    ret1 = []
    for i in range(m_a_dim[0]):
        ret2 = []
        for j in range(m_b_dim[1]):
            appe = 0
            for k in range(m_a_dim[1]):
                appe += (m_a[i][k] * m_b[k][j])
            ret2.append(appe)
        ret1.append(ret2)
    return ret1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
