#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    if n >= 0 and n < len(str):
        for i in range(0, n):
            new += str[i]
        for i in range(n + 1, len(str)):
            new += str[i]
    else:
        new = str
    return (new)
