#!/usr/bin/python3
for a in range(97, 123):
    if a != ord('q') and a != ord('e'):
        print("{:c}".format(a), end='')
