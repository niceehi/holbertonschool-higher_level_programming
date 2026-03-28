#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    count = len(args)

    if count == 0:
        print("Number of arguments.")
    elif count == 1:
        print("Number of argument: 1")
    else:
        print(f"Number of arguments: {count}")

    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")
