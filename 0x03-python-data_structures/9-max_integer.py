#!/usr/bin/python3
def max_integer(my_list=[]):
    maxNum = 0
    for x in my_list:
        if x > maxNum:
            maxNum = x
    return maxNum
