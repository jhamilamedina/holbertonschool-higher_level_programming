#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    lenArgc = len(argv) - 1
    strArgs = 'arguments:'

    if lenArgc == 0:
        strArgs = 'arguments.'
    elif lenArgc == 1:
        strArgs = 'argument:'

    print("{0} {1}".format(lenArgc, strArgs))

    for i in range(1, lenArgc + 1):
        print("{0}: {1}".format(i, argv[i]))
