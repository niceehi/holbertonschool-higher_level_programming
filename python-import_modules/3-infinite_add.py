#!/usr/bin/python3

from sys import argv
sum = 0
if __name__ == "__main__":
    for i in range(len(argv)):
        sum = sum + argv[i]
    print(sum)
