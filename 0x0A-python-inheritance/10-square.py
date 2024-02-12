#!/usr/bin/python3
"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits Rectangle class"""
    def __init__(self, size):
        """
        initializes square
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns area of the square
        """
        return self.__size * self.__size
