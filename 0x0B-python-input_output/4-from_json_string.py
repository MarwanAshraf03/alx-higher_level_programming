#!/usr/bin/python3
"""From JSON String Module"""


def from_json_string(my_str):
    """
    returns object from JSON string representation
    """
    import json
    return json.loads(my_str)
