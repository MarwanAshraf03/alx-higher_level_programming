#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, x):
        return self != x
    def __ne__(self, x):
        return self == x