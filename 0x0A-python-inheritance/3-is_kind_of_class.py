#!/usr/bin/python3
"""Is Kind of Class Module"""


def is_kind_of_class(obj, a_class):
    """
    determines if the obj is an instance of,
    or if the object is an instance of a class that inherited from
    a_class
    """
    return isinstance(obj, a_class)
