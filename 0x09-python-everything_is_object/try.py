#!/usr/bin/python3
s1 = [1, 2]
s2 = s1
print(s1 == s2)
print(s1 is s2)
s2 += [3, 4]
print(s1 == s2)
print(s1 is s2)