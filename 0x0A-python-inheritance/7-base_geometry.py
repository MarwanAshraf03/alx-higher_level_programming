#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry():
    """Improved BaseGeometry class"""

    def area(self):
        """
        area method raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value to be integer

        Args:
        name: name of the value
        value: value to be evaluated
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
