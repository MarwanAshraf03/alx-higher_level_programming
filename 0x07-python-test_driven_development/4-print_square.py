#!/usr/bin/python3
"""Print Square Module"""


def print_square(size):
    """
    prints square of perimeter size * size

    Args:
    size: the side length of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
