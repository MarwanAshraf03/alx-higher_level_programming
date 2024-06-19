#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    from urllib import request
    import sys
    with request.urlopen(sys.argv[1]) as response:
        for i in response.getheaders():
            if i[0] == 'X-Request-Id':
                print(i[1])
