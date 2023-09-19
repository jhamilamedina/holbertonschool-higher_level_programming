#!/usr/bin/python3
def uppercase(str):
    n = [chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in str]
    print("{0}".format("".join(n)))
