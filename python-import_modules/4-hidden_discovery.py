#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    listh = [c for c in dir(hidden_4) if c[0] != '_']
    listh.sort()

    for i in listh:
        print(i)
