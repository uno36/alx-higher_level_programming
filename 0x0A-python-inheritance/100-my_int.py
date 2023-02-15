#!/usr/bin/python3
class MyInt(int):
    """a class MyInt that inherits from int"""
    def __eq__(self, other):
        """return false if true"""
        return False

    def __ne__(self, other):
        """return true if false"""
        return True
