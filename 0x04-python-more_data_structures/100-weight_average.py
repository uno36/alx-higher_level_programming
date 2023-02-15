#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    result = 0
    d = 0
    for tuple_list in my_list:
        result += tuple_list[0] * tuple_list[1]
        d += tuple_list[1]
    return result/d
