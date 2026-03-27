#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            c = chr(ord(char) - 32)
        print("{}".format(c), end="")
    print()
