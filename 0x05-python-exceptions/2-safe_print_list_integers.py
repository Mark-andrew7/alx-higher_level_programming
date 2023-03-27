#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            result = int(my_list[i])
            print("{:d}".format(result), end="")
            count += 1
            i += 1
        except(ValueError, TypeError):
            pass
            print()
            return count
