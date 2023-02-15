#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in range(0, len(new)):
        if new[i] == search:
            new[i] = replace
    return new
