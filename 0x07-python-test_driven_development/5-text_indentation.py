#!/usr/bin/python3
"""Module to prints a text
"""


def text_indentation(text):
    """ This function  prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text: string text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = ""
    for i in text:
        if i == "\n":
            print("{}".format(new))
            new = ""
            continue
        else:
            new += i
        if i == '.' or i == '?' or i == ':':
            new = new.strip(" ")
            print("{}".format(new), end="")
            print("\n")
            new = ""
    new = new.strip(" ")
    print("{}".format(new), end="")
