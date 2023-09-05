#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer()"""
    def test_noArgs(self):
        """Test for no arguments"""
        self.assertEqual(max_integer(), None)

    def test_emptyList(self):
        """Test for no arguments"""
        self.assertEqual(max_integer([]), None)

    def test_oneElementInList(self):
        """Test for no arguments"""
        self.assertEqual(max_integer([1]), 1)

    def test_twoRepeatedElements(self):
        """Test for no arguments"""
        self.assertEqual(max_integer([1, 2, 2]), 2)

    def test_tupleOneElement(self):
        """Test for no arguments"""
        self.assertEqual(max_integer((2, )), 2)

    def test_tupleMultipleElements(self):
        """Test for no arguments"""
        self.assertEqual(max_integer((2, 4)), 4)

    def test_string(self):
        """Test for no arguments"""
        self.assertEqual(max_integer("True"), "u")

    def test_stringList(self):
        """Test for no arguments"""
        self.assertEqual(max_integer(["True", "False", "School"]), "True")

    def test_wrongArgs(self):
        """Test for no arguments"""
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 2j)
        self.assertRaises(TypeError, max_integer, [True, "True", 3.5, 2])

    def test_intAndFloat(self):
        """Test for no arguments"""
        self.assertEqual(max_integer([1, 3.9, 3.5, 2]), 3.9)
