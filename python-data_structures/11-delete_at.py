#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = []
    for i in range(0, my_list):
        if (i == 0):
            new_list.append(my_list[i])
    return new_list
