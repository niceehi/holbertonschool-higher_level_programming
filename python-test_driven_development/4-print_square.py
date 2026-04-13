#!/usr/bin/python3
"""Prints a square using the # character."""


def print_square(size):
    """Prints a square of size x size with #."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
