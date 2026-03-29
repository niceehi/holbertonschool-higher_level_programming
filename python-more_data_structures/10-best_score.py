#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
         return None

    b_key = None
    max_value = None
    for key, value in a_dictionary.items():
        if max_value is None  or value > max_value:
            max_value = value
            b_key = key
    return b_key
