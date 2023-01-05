#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result -= 32
    print("{:s}".format(result), end="")
    print("")
