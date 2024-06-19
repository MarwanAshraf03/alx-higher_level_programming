#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    import requests
    import sys
    resp = requests.get(sys.argv[1])
    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    else:
        print(resp.content.decode('utf-8'))
