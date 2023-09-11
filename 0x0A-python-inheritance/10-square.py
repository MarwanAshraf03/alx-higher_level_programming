#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Square Module"""


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
