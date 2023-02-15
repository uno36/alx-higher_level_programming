#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = ':'
    a = 'arguments'
    if len(sys.argv) == 1:
        c = '.'
    if len(sys.argv) == 2:
        a = 'argument'
    print("{:d} {:s}{:s}".format(len(sys.argv) - 1, a, c))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
