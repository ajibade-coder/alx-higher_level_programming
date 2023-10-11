#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    demerator = 0
    for x , y in my_list:
        numerator += x * y
        demerator += y 
    return numerator / demerator
