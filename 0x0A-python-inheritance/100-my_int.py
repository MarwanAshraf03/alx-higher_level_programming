#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, x):
        return self != x