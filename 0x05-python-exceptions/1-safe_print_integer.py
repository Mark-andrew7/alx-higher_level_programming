#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print()
        return true
    except(ValueError):
        return false
