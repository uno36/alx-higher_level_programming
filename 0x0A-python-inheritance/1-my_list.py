#!/usr/bin/python3
class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """print a sorted list"""
        print("{}".format(sorted(self)))
