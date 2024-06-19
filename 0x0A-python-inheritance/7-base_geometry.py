#!/usr/bin/python3
"""Improved BaseGeometry Module"""


class BaseGeometry:
    """Improved BaseGeometry class"""

    def area(self):
        """
        area method raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value to be int

        Args:
        name: name of the value
        value: value to be evaluated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
