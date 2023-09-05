#!/usr/bin/python3
def print_square(size):
    if type(size).__name__ in ("int", "float"):
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
        