#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    import requests
    from urllib import parse
    import sys
    values = {'email': sys.argv[2]}
    requests.post(sys.argv[1], values)
