#!/usr/bin/python3
def uppercase(str):
    for char in str:
        result = ord(char)
        if result > 96 and result < 123:
            result -= 32
    print("{}".format(chr(result)), end="")
    print("")
