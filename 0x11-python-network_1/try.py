"""To fetch https://alx-intranet.hbtn.io/status"""
from urllib import request
import sys
with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    for i in response.getheaders():
        if i[0] == 'X-Request-Id':
            print(i[1])
    # resp = response.read()
# print(dir(response))
# print(response.getheaders())