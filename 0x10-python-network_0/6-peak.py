#!/usr/bin/python3
"""A module to find pead of list"""


def find_peak(list_of_integers):
    """the method to find the peak of the list"""
    if (len(list_of_integers)) == 0:
        return None
    if len(list_of_integers) > 1:
        return max(list_of_integers[0], find_peak(list_of_integers[1:]))
    else:
        return list_of_integers[0]


def max(x, y):
    return x if x > y else y
