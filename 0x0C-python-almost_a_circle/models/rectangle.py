#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.__width = width
        self.__heigth = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        return self.__width

    @width.setter
    def set_width(self, width):
        self.__width = width

    @property
    def get_height(self):
        return self.__heigth

    @heigth.setter
    def set_height(self, height):
        self.__heigth = height

    @property
    def get_x(self):
        return self.__x

    @x.setter
    def set_height(self, x):
        self.__x = x

    @property
    def get_height(self):
        return self.__y

    @y.setter
    def set_height(self, y):
        self.__y = y
