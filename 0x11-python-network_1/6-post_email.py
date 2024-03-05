#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    import requests
    from urllib import parse
    import sys
    values = {'email': sys.argv[2]}
    resp = requests.post(sys.argv[1], values)
    print(resp.content.decode('utf-8'))
