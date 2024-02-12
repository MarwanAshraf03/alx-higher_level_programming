#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    le = len(my_list) - 1
    while le != -1:
        print("{:d}".format(my_list[le]))
        le -= 1
