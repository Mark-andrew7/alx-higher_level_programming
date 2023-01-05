#!/usr/bin/python3
def pow(a, b):
    result = 1
    while b != 0:
        result *= a
        b-=1
    print("" + "{s}".format(result), end="")
