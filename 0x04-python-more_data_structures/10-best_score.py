#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key = list(a_dictionary.keys())
    value = list(a_dictionary.values())
    return key[value.index(max(value))]
