#!/usr/bin/python3
"""Load From JSON File Module"""


def load_from_json_file(filename):
    """
    loads object from json file

    Args:
    filename: name of json file
    """
    import json
    with open(filename, "r", encoding="UTF8") as f:
        return json.load(f)
