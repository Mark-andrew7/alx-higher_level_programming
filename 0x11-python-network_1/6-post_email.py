#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    res = requests.get(url, data=value)
    print(res.text)
