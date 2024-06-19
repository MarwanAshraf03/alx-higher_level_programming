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

    @property
    def size(self):
        """Getter for __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size

        Args:
            value: new value of __size
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns area of square"""
        return self.__size*self.__size

    def my_print(self):
        """Prints square with #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
