#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            len += 1
    except (IndexError, TypeError, ValueError):
        pass
    print()
    return len
