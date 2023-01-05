#!/usr/bin/python3
def uppercase(str):
    for char in str:
        result = ord(char)
        if result >= 97 and result <= 122:
            result -= 32
    print("{:s}".format(result), end="")
    print("")
