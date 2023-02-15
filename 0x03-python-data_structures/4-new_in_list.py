#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for i in my_list[:]:
        if i == my_list[idx]:
            new_list.append(element)
        else:
            new_list.append(i)
    return new_list
