#!/usr/bin/python3
"""A module to find pead of list"""
def find_peak(list_of_integers):
    """the method to find the peak of the list"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    # if len(list_of_integers) == 2:
    return max(find_peak(list_of_integers[int(len(list_of_integers)/2):]), find_peak(list_of_integers[:int(len(list_of_integers)/2)+1]))

    # else:
    #     find_peak(list_of_integers[:int(len(list_of_integers)/2)])
    #     find_peak(list_of_integers[int(len(list_of_integers)/2):])

def max(x, y):
    """find maximum of two numbers"""
    return x if x > y else y