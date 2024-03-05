#!/usr/bin/python3
"""Find X-Request-Id value"""
if __name__ == "__main__":
    import requests
    # import requests.exceptions.JSONDecodeError
    from requests import exceptions
    import sys
    data = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {sys.argv[2]}",
    "X-GitHub-Api-Version": "2022-11-28"
    }
    resp = requests.post(f"https://api.github.com/users/{sys.argv[1]}", data=data)
