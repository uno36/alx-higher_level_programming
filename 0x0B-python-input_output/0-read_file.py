#!/usr/bin/python3
def read_file(filename=""):
    """
    Write a function that reads a text file
    (UTF8) and prints it to stdout.
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
