#!/usr/bin/env python3
"""To fetch https://alx-intranet.hbtn.io/status"""
from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    resp = response.read()
print(resp.length)
print(resp.peek())
print(resp)
data = resp.read()
