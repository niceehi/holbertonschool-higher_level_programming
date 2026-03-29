#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    uniq_numbers = []
    for i in my_list:
        if i not in uniq_numbers:
            sum = sum + i
    return sum
