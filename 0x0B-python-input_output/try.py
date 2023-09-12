#!/usr/bin/python3
l = ["s", "k", "y"]

bool = all([isinstance(i, str)] for i in l)
print(bool)