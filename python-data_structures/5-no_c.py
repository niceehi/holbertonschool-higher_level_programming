#!/usr/bin/python3

new_string = []
def no_c(my_string):
    for i in my_string:
        if i != 'c':
            new_string.append(my_string[i])
    return new_string
