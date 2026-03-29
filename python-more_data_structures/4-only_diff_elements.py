#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    only = set()
    for i in set_1:
        if i not in set_2:
            only.add(i)

    for i in set_2:
        if i not in set_1:
            only.add(i)
    return only
