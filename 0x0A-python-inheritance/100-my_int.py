#!/usr/bin/python3
"""My Int Module"""


class MyInt(int):
    """MyInt class inherits int class"""
    def __eq__(self, x):
        """overloads == to !="""
        return super().__ne__(x)

    def __ne__(self, x):
        """overloads != to =="""
        return super().__eq__(x)
