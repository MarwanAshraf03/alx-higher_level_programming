#!/usr/bin/python3
l = ["fName", "age", "hi"]
d = {
    "fName": "jack",
    "lName": "sparrow",
    "age": 19
}

for i in l:
    if i in d.keys():
        print(d[i])