#!/usr/bin/python3
def max_integer(my_list=[]):
     if not my_list:
        return None
    else:
        maxNum = 0
        for x in my_list:
            if x > maxNum:
                maxNum = x
        return maxNum
