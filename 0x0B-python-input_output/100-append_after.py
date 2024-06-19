#!/usr/bin/python3
"""Append After Module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends new string after finding search string

    Args:
    filename: name of file
    search_string: string to search for
    new_string: string to be appended
    """
    w = ''
    with open(filename, "r", encoding="UTF8") as f:
        for i in f.readlines():
            w += i
            if search_string in i:
                w += new_string
    with open(filename, "w", encoding="UTF8") as f:
        f.write(w)
