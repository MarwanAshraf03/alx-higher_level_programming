#!/usr/bin/python3
"""'Inherits From' Module"""


def inherits_from(obj, a_class):
    """
    determines if the object
    is an instance of a class that
    inherited (directly or indirectly)
    from the specified class
    """

    return (isinstance(obj, a_class)) & (type(obj) is not a_class)
