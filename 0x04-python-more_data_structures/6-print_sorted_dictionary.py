#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keysort = sorted(a_dictionary)
    for x in keysort:
        print("{}: {}".format(x, a_dictionary[x]))
