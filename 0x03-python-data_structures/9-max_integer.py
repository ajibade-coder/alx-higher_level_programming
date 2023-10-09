#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None:
        return None
    else:
        maxNum = 0
        for x in my_list:
            if x > maxNum:
                maxNum = x
        return maxNum
