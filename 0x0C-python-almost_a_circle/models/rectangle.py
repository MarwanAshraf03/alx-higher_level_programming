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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__heigth

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__heigth = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("x must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints rectangle with # character"""
        for i in range(self.height):
                print(self.width * "#")
