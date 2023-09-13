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
    with open(filename, "r", encoding="UTF8") as f:
        lis = f.readlines()
    for i in range(len(lis)):
        if lis[i].find(search_string) >= 0:
            lis.insert(i+1, new_string)
    print(lis)

    with open(filename, "w", encoding="UTF8") as f:
        for i in lis:
            f.write(i)
