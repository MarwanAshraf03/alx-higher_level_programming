#!/usr/bin/python3
"""To fetch https://alx-intranet.hbtn.io/status"""
import requests
resp = requests.get('https://alx-intranet.hbtn.io/status')
print(f"Body response:\n\t\
- type: {type(resp.content.decode('utf-8'))}\n\t\
- content: {resp.content.decode('utf-8')}")
