#!/usr/bin/python3
"""Print Square Module"""


def print_square(size):
    """
    prints square of perimeter size * size

    Args:
    size: the side length of square
    """
    if type(size).__name__ in ("int"):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be >= 0")
        if isinstance(size, int) and size < 0:
            raise ValueError("size must be >= 0")
        size = int(size)
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    else:
        raise TypeError("size must be an integer")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
