#!/usr/bin/python3
"""Write File Module"""


def write_file(filename="", text=""):
    """
    Writes to file

    Args:
    filename: name of the file
    text: string to be written

    Return:
    returns number of characters written
    """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
