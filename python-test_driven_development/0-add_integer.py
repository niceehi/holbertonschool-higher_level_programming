#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.

    a and b must be int or float, otherwise raise TypeError.
    Floats are cast to int before addition.
    NaN values are not allowed.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and a != a:
        raise ValueError("a cannot be NaN")
    if isinstance(b, float) and b != b:
        raise ValueError("b cannot be NaN")

    return int(a) + int(b)
