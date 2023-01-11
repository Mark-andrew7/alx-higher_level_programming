#!/usr/bin/python3

from sys import argv

i, res = 1, 0

if __name__ == "__name__":
    while i < len(argv):
        res += int(argv[i])
        i += 1
    print(res)
