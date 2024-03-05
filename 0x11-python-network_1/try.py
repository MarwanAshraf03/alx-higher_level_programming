"""Find X-Request-Id value"""
if __name__ == "__main__":
    from urllib import request
    from urllib import error
    import sys
    try:
        with request.urlopen("https://www.google.com/404") as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(dir(e))
        print(e.code)
