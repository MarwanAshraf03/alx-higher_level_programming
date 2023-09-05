#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_noArgs(self):
        self.assertEqual(max_integer(), None)
    def test_emptyList(self):
        self.assertEqual(max_integer([]), [])
    def test_oneElementInList(self):
        self.assertEqual(max_integer([1]), [])