#!/usr/bin/python3
"""Lookup Module"""


def lookup(obj):
    """
    Lookup Method

    Args:
    obj: an object to be used

    Returns:
    returns a list of available
    methods and attributes of obj
    """

    return dir(obj)
