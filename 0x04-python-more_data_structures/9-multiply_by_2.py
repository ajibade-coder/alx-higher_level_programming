#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for x, y in new_dic.items():
        new_dic[x] = y * 2
    return new_dic
