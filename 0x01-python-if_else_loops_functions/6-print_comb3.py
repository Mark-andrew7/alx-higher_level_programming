#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        print("{:0d}{1:d}".format(i, j), end=", " if j < 9 else "\n")
