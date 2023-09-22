#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    ln = len(argv)
    ar = 0

    if ln != 1:
        for i in range(1, ln):
            ar += int(argv[i])
    print("{}".format(ar))
