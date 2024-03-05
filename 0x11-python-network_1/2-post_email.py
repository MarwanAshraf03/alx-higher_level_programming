#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    from urllib import request
    import sys
    with request.urlopen(request.Request(sys.argv[1], sys.argv[2].encode('ascii'))) as response:
        print(response.read().decode('utf-8'))
