#!/usr/bin/python3
"""Append Write Module"""


def append_write(filename="", text=""):
    """
    Appends text to a file

    Args:
    filename: name of the file
    text: string to be appended

    Return:
    returns number of characters added
    """
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
