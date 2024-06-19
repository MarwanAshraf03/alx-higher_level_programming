#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    import requests
    import sys
    data = (sys.argv[1], sys.argv[2])
    resp = requests.get("https://api.github.com/user", auth=data)
    try:
        print(resp.json()['id'])
    except Exception:
        print("None")
