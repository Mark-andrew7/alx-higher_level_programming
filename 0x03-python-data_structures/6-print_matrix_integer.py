#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                if y != len(matrix[x]) - 1:
                    print("{:d}".format(matrix[x][y]), end=" ")
                else:
                    print("{:d}".format(matrix[x][y]))
    else:
        print()
