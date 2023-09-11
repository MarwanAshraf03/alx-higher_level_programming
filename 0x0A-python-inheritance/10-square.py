#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Square Module"""


class Square(Rectangle):
    """Square class inherits Rectangle class"""
    def __init__(self, size):
        """
        initializes square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns area of the square
        """
        return self.__size * self.__size
