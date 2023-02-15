#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename) as f:
        num_line = sum(1 for line in f)
    f.closed
    return num_line
