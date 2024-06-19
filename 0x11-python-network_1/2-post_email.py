#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    from urllib import request
    from urllib import parse
    import sys
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
