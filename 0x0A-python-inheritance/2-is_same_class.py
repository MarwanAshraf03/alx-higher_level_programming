#!/usr/bin/python3
"""Is Same Class Module"""


def is_same_class(obj, a_class):
    """
    determines if the object is exactly an instance of the specified class
    """

    return type(obj) is a_class
