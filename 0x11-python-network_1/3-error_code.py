#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Handles HTTPError exceptions and prints the HTTP status code.
"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
