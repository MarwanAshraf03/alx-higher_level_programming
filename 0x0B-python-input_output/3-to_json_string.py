#!/usr/bin/python3
"""To JSON String Module"""


def to_json_string(my_obj):
    """
    returns string representation of object
    """
    import json
    return json.dumps(my_obj)
