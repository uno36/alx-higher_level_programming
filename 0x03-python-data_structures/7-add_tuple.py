#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = 2 - len(tuple_a)
    if a0 >= 0:
        for i in range(0, a0):
            tuple_a = tuple_a + (0,)

    b0 = 2 - len(tuple_b)
    if b0 >= 0:
        for i in range(0, b0):
            tuple_b = tuple_b + (0,)
    sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum
