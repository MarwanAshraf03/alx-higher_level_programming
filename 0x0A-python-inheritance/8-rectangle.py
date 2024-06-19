#!/usr/bin/python3
"""Rectangle Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectanlge class inherits BaseGeometry class
    """

    def __init__(self, width, height):
        """
        __init__ method
        initiates rectangle
        Args:
        width: rectangle width
        height: rectangle height
        """

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
