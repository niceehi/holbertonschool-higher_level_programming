#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    
    max_el = my_list[0]
    for i in my_list:
        if i > max_el:
            max_el = i
    return max_el
