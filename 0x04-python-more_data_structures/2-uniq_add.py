#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    answer = 0
    for x in new:
        answer += x
    return answer
