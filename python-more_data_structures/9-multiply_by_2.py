#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_d = {}
    for i, j in a_dictionary.items():
        new_d[i] = j * 2
    return new_d
