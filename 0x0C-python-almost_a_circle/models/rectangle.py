#!/usr/bin/python3
from models.base import Base
"""Rectangle Module"""


class Rectangle(Base):
    """Rectangle class inherits Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes rectangle with values

        Args:
        width: width of the rectangle
        height: height of the rectangle
        x: vertical indent of rectangle
        y: horizontal indent of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__heigth

    @height.setter
    def height(self, height):
        """height setter"""
        self.__heigth = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.__y = y
