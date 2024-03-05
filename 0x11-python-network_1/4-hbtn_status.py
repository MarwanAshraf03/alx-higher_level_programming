#!/usr/bin/python3
"""To fetch https://alx-intranet.hbtn.io/status"""
import requests
resp = requests.get('https://alx-intranet.hbtn.io/status')
print(f"Body response:\n\t\
- type: {type(resp)}\n\t\
- content: {resp}\n\t\
- utf8 content: {resp.decode('utf-8')}")
