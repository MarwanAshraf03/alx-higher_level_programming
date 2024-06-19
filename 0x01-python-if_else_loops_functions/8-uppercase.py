#!/usr/bin/python3
def islower(char):
    return ((ord(char) >= ord('a')) and (ord(char) <= ord('z')))


def uppercase(str):
    for char in str:
        print(
            "{:c}".format(
                ord(char)
                if not islower(char) else (ord(char) - 32)
                ), end=""
        )
    print("")
