#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tmp = 0
    len = 0
    while True:
        try:
            for i in range(tmp, x):
                print("{:d}".format(my_list[i]), end="")
                len += 1
            print()
            return (len)
        except (TypeError, ValueError):
            tmp = i + 1
            pass
