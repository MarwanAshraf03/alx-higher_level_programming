#!/usr/bin/python3
"""Save To JSON File Module"""


def save_to_json_file(my_obj, filename):
    """
    Saves string representation of my_obj
    to filename

    Args:
    my_obj: object to be seralized
    filename: name of json file
    """
    import json
    with open(filename, "w", encoding="UTF8") as f:
        json.dump(my_obj, f)
