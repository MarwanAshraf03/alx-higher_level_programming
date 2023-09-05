#!/usr/bin/python3
"""An add_integer module to add two numbers"""


def add_integer(a, b=98):
    """
    adds two integer or float numbers

    Args:
        a: first number to be added
        b: second number to be added
    Return:
    a + b
    """
    if type(a).__name__ not in ("int", "float"):
        raise TypeError("a must be an integer")
    if type(b).__name__ not in ("int", "float"):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
