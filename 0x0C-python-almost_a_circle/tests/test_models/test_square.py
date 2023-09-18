#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Base Testing"""


class test_base(unittest.TestCase):
    
    def instantiation(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def ch_private_nb_objects(self):
        b = Base()
        self.assertRaises(TypeError, b.__nb_objects)

if __name__ == '__main__':
    unittest.main()