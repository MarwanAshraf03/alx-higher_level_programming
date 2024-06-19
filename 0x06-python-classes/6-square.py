#!/usr/bin/python3
"""Square Module 2."""


class Square:
    """Defines a Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square

        Args:
            size: length of side
            position: position of printing the square
        """
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(position[0], int)) | (
            not isinstance(
                position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 & position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([x for x in position if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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

    @property
    def position(self):
        """Getter for __position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Setter for __position

        Args:
            value: new value of __size
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 & value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of square"""
        return self.__size*self.__size

    def my_print(self):
        """Prints square with #"""
        if self.__size == 0:
            print()
            return
        print(self.__position[1]*"\n", end='')
        for i in range(self.__size):
            print(self.__position[0]*" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
