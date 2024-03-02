#!/usr/bin/python3
"""A module to find pead of list"""


def find_peak(list_of_integers):
    """the method to find the peak of the list"""
    if (len(list_of_integers)) == 0:
        return None
    return max(list_of_integers)
