#!/usr/bin/python3
"""
import unittest module
"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """
        tests max integer from a list
        """
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)

    def test_none(self):
        """
        returns None as no argument is parsed
        """
        self.assertEqual(max_integer([]), None)

    def test_max_at_begginning(self):
        """
        tests for max int at begginning
        """
        self.assertEqual(max_integer([10, 8, 6, 1]), 10)

    def test_negative(self):
        """
        test for negative numbers
        """
        self.assertEqual(max_integer([-4, -6, -8, -1]), -1)

    def test_one_element(self):
        """
        test for one element in a list
        """
        self.assertEqual(max_integer([10]), 10)

    def test_one_negative(self):
        """
        test where one negative is in a list
        """
        self.assertEqual(max_integer([-1, 2, 4, 6]), 6)
