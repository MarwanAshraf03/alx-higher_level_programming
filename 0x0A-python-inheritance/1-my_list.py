#!/usr/bin/python3
"""My List Module"""


class MyList(list):
    """
    Class MyList inherits list class
    """
    def print_sorted(self):
        """
        Prints sorted Mylist
        """

        print(sorted(self))
