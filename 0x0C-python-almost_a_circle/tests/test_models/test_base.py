#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Base Testing"""


class TestBase(unittest.TestCase):
    """Define unittests for testing of the Base class"""

    def re(self):
        """Reset nb_instances to 0"""
        Base._Base__nb_objects = 0
        pass

    def test_instantiation(self):
        b = Base()
        self.assertIsInstance(b, Base)
        self.re()

    def test_private_nb_objects(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b3.id, 3)
        self.re()

    def test_assign_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)
        self.re()


if __name__ == '__main__':
    unittest.main()
