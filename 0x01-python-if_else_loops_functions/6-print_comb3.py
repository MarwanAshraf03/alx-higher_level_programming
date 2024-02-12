#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i == 8 and j == 9:
            break
        if i < j:
            print("{}{}, ".format(i, j), end="")
    if i == 8 and j == 9:
        break
print("{}{}".format(8, 9))
