#!/usr/bin/python3

def add_integer(a, b=98):

    if isinstance(a, int):
        raise TypeError("a must be an integer or b must be an integer")

    elif isinstance(a, float):
        a = int(a)

    return a + b
