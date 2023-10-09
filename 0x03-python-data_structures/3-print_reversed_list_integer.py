#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    total = len(my_list) - 1
    while 0 <= total:
        print("{}".format(my_list[total]))
        total -= 1
