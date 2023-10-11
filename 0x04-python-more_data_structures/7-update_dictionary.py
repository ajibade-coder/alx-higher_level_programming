#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for x in a_dictionary:
        if x == str(key):
            a_dictionary[x] = value
    a_dictionary[key] = value
    return a_dictionary
