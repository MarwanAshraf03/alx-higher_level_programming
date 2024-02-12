#!/usr/bin/python3
"""Square Module 2."""


class Square:
    """Defines a Square."""
    def __init__(self, size=0):
        """Initialize Square

        Args:
            size: length of side
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
