#!/usr/bin/python3
"""Class To JSON Module"""


def class_to_json(obj):
    """returns dictionary representation of object"""
    return (vars(obj))
