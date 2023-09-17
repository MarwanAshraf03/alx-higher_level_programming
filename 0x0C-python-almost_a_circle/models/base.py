#!/usr/bin/python3
"""Base Module"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes Base class with id

        Args:
        id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
