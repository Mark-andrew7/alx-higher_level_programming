#!/usr/bin/python3

import sys
if __name__ == "__main__":
    n = len(sys.argv)
    res = 0
    for i in range(1, n):
        res += len(sys.argv[i])
    print(res)
