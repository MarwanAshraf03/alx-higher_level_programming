#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    ret = ""
    m = -1
    for i in a_dictionary:
        if a_dictionary[i] > m:
            m = a_dictionary[i]
            ret = i
    return ret
