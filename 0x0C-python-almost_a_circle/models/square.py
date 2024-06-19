#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """Size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updates square with given values"""
        if args and len(args) > 0:
            for i in range(len(args)):
                if (i == 0) and (args[i] is not None):
                    self.id = args[i]
                if (i == 1) and (args[i] is not None):
                    self.size = args[i]
                if (i == 2) and (args[i] is not None):
                    self.x = args[i]
                if (i == 3) and (args[i] is not None):
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary of attributes of square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y}
