#!/usr/bin/python3
"""To fetch https://alx-intranet.hbtn.io/status"""
from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    resp = response.read()
print(f"Body response:\n\t\
- type: {type(resp)}\n\t\
- content: {resp}\n\t\
- utf8 content: {resp.decode('utf-8')}")
