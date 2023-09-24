#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for i in matrix:
            u = 1
            for o in i:
                if u < len(i):
                    print("{:d} ".format(o), end='')
                else:
                    print("{:d}".format(o))
                u += 1
    else:
        print()
