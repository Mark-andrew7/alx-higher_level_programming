#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    large = my_list[0]
    for x in range(1, len(my_list)):
        if large < my_list[x]:
            large = my_list[x]
        else:
            continue
    return large
