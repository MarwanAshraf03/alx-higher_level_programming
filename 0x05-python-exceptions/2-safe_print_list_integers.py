#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    iterator, count = 0, 0
    while iterator < x:
        try:
            print("{:d}".format(my_list[iterator]), end='')
            count += 1
        except (ValueError, TypeError):
            pass
        iterator += 1
    print("\n", end='')
    return count
