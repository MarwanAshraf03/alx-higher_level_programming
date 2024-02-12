#!/usr/bin/python3
"""Say My Name Module"""


def say_my_name(first_name, last_name=""):
    """
    prints 'My name is <first name> <last name>'

    Args:
    first_name: first name string
    last_name: last name string
    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name:s} {last_name:s}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
