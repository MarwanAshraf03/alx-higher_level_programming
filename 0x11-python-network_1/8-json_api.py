#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) > 1:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
    resp = requests.post("http://0.0.0.0:5000/search_user", values)
    # print(dir(resp))
    print(resp.json)
    # print(resp.content)
    # print(type(resp.content.decode('utf-8')))
    # print(resp.content.decode('utf-8'))
    # print(dict(resp.content.decode('utf-8')))
