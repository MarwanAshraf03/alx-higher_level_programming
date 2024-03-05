#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    import requests
    import sys
    # resp = requests.get(sys.argv[1])
    resp = requests.get("https://intranet.alxswe.com/projects/300")
    print(dir(resp))
    # if resp.cod
    # print(response.read().decode('utf-8'))
    # except error.HTTPError as e:
    #     print(f"Error code: {e.code}")
