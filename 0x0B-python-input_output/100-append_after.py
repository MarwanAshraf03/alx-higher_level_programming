#!/usr/bin/python3
"""Pascal's Triangle Module"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "a+", encoding="UTF8") as f:
        lstr = [*search_string]
        for line in f.readline():
            lline = [*line]
            return
    pass