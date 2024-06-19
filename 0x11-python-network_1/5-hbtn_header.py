#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    import requests
    import sys
    resp = requests.get(sys.argv[1]).headers
    if 'X-Request-Id' in resp.keys():
        print(resp['X-Request-Id'])
