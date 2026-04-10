#!/usr/bin/python3
"""Module that provides a function to add two integers."""


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.

    a and b must be int or float, otherwise raise TypeError.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
