#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = my_list[:]
    if idx >= 0 and idx < len(my_list):
        n[idx] = element

    return n
