#!/usr/bin/python3

def pow(a, b):
    while b != 1:
        a = a * a
        if b > 0:
            b = b - 1
        else:
            b = b + 1
    return a
