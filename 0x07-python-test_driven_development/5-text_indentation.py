#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in ".?:":
        text = text.replace(i, i + "\n\n")
    print('\n'.join(t.strip() for t in text.split('\n')), end='')
