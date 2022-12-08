#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda new: new if new != search else replace, my_list))
