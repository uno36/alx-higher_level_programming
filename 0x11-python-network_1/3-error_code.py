#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and displays
# the body of the response (decoded in utf-8).
if __name__ == "__main__":
    import urllib
    from urllib import request, parse
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
