#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set(my_list)
    uniq_list = list(set_list)
    sum = 0
    for i in uniq_list:
        sum += i
    return sum
