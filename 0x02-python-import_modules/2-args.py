#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(0))
    elif len(sys.argv) == 2:
        print("{} argument:\n{}: {}".format(1, 1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
