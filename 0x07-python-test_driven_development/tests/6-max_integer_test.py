#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a class testMax that test the max_integer function
    """

    def test_successCase(self):
        """This function test all the success case
         """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 6, 4]), 6)
        self.assertEqual(max_integer("bnxfz"), "z")
        self.assertEqual(max_integer("AnZfz"), "z")
        self.assertEqual(max_integer(["a", "c", "z"]), "z")
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-1, -5, -3]), -1)
        self.assertEqual(max_integer([1]), 1)
if __name__ == '__main__':
    unittest.main()
