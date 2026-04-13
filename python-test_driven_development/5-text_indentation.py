#!/usr/bin/python3
"""This module defines a text indentation function."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    skip_space = True

    while i < len(text):
        char = text[i]

        if skip_space and char == " ":
            i += 1
            continue

        skip_space = False

        print(char, end="")

        if char in ".?:":
            print("\n")
            skip_space = True

        i += 1
