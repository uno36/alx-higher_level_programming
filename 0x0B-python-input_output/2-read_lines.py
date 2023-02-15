#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """read n lines of a text file (UTF8) and prints it to stdout
    Args:
       filename: name of the file
       nb_lines: number of lines that need to read
    """
    with open(filename) as f:
        for line in f:
            nb_lines -= 1
            print("{}".format(line), end="")
            if nb_lines == 0:
                break
