#!/usr/bin/python3
for i in range(0, 10):
    for o in range(0, 10):
        if i != o and o > i:
            if i + o != 17:
                print("{0}{1}, ".format(i, o), end='')
            else:
                print("{0}{1}".format(i, o))
