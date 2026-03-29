#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_2 = [len(my_list)]
    for i in range(0, len(my_list)):
        my_2[i] = my_list[i]
    my_2 [idx] = element
    return my_2
