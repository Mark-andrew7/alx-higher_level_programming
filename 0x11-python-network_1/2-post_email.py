#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
