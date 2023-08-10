#!/usr/bin/python3
def islower(c):
    return ((ord(c) >= ord('a')) and (ord(c) <= ord('z')))


def uppercase(str):
    for c in str:
        if islower(c):
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{}".format(c), end="")
    print("")
