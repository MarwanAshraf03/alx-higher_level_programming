#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Define unittests for testing of the Base class"""

    def re(self):
        """Reset nb_instances to 0"""
        Base._Base__nb_objects = 0
        pass

    def test_instantiation(self):
        """test instantiation"""
        b = Base()
        self.assertIsInstance(b, Base)
        self.re()

    def test_private_nb_objects(self):
        """test that nb_objects is private"""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_auto_id(self):
        """test auto assignment of id of instances"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b3.id, 3)
        self.re()

    def test_assign_id(self):
        """test assigning id manually"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)
        self.re()

    def test_to_json_string(self):
        """test to_json_string function with normal input"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

    def test_to_json_string_empty(self):
        """test to_json_string function with empty list"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_None(self):
        """test to_json_string function with 'None' input"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")


if __name__ == '__main__':
    unittest.main()
