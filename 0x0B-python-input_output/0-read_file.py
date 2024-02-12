#!/usr/bin/python3
"""Read File Module"""


def read_file(filename=""):
    """Reads file and prints it to the stdout"""
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read(), end='')
