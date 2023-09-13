#!/usr/bin/python3
"""Pascal's Triangle Module"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "a+", encoding="UTF8") as f:
        for line in f.readline():
            if line.find(search_string) >= 0:
                f.write(new_string)
