#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


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
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

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
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints rectangle with # character"""
        str = self.y * "\n" + (self.height * (
            (self.x * " ") + self.width * "#" + '\n'
            ))
        print(str[:-1])

    def __str__(self):
        """Returns String representation of Rectangle"""
        return f"[Rectangle]" +\
            f" ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """updates instance with given arguments"""
        if args and len(args) > 0:
            for i in range(len(args)):
                if (i == 0) and (args[i] is not None):
                    self.id = args[i]
                if (i == 1) and (args[i] is not None):
                    self.width = args[i]
                if (i == 2) and (args[i] is not None):
                    self.height = args[i]
                if (i == 3) and (args[i] is not None):
                    self.x = args[i]
                if (i == 4) and (args[i] is not None):
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary of attributes of rectangle"""
        return {
            "x": self.__x,
            "width": self.__width,
            "id": self.id,
            "height": self.__height,
            "y": self.__y}
