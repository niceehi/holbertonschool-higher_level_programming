#!/usr/bin/python3

def print_last_digit(number):
    if (number > 0):
        r = number % 10
    else:
        number = number % 10
        r = number + 10
    return r
