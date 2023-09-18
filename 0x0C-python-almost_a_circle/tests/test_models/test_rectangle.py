#!/usr/bin/python3
"""Unittest for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define unittests for testing instantiation of the Rectangle class"""

    def re(self):
        """Reset nb_instances to 0"""
        Base._Base__nb_objects = 0
        pass

    def test_instantiation_with_None(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_instantiation_with_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle(12)

    def test_instantiation_with_width_wrong(self):
        with self.assertRaises(TypeError):
            r = Rectangle('13', '12')

    def test_instantiation_with_width_wrong2(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, '12')

    def test_instantiation_with_width_wrong3(self):
        with self.assertRaises(TypeError):
            r = Rectangle(13.5, '12')

    def test_instantiation_with_width_wrong4(self):
        with self.assertRaises(TypeError):
            r = Rectangle((13.5, ), '12')

    def test_instantiation_with_width_wrong5(self):
        with self.assertRaises(TypeError):
            r = Rectangle([13.5], '12')

    def test_instantiation_with_width_wrong6(self):
        with self.assertRaises(TypeError):
            r = Rectangle({}, '12')

    def test_instantiation_with_height_wrong(self):
        with self.assertRaises(TypeError):
            r = Rectangle(12, '12')

    def test_instantiation_with_height_wrong2(self):
        with self.assertRaises(ValueError):
            r = Rectangle(12, -1)

    def test_instantiation_with_height_wrong3(self):
        with self.assertRaises(TypeError):
            r = Rectangle(12, 13.5)

    def test_instantiation_with_height_wrong4(self):
        with self.assertRaises(TypeError):
            r = Rectangle(12, (13.5,))

    def test_instantiation_with_height_wrong5(self):
        with self.assertRaises(TypeError):
            r = Rectangle(12, [13.5])

    def test_instantiation_with_height_wrong6(self):
        with self.assertRaises(TypeError):
            r = Rectangle(12, {})

    def test_instantiation_with_width_and_height(self):
        r = Rectangle(12, 13)
        self.assertEqual(r.width, r.height - 1)

    def test_instantiation_full(self):
        r = Rectangle(12, 13, 0, 1, 14)
        self.assertEqual(r.width, r.height - 1)
        self.assertEqual(r.x, r.y - 1)
        self.assertEqual(r.id, 14)

    def test_width_getter(self):
        r = Rectangle(15, 16)
        self.assertEqual(r.width, 15)

    def test_width_setter(self):
        r = Rectangle(15, 16)
        r.width = 20
        self.assertEqual(r.width, 20)

    def test_height_getter(self):
        r = Rectangle(15, 16)
        self.assertEqual(r.height, 16)

    def test_height_setter(self):
        r = Rectangle(15, 16)
        r.height = 20
        self.assertEqual(r.height, 20)
        
    def test_x_getter(self):
        r = Rectangle(15, 16, 3, 1)
        self.assertEqual(r.x, 3)

    def test_x_setter(self):
        r = Rectangle(15, 16, 3, 1)
        r.x = 1
        self.assertEqual(r.x, 1)

    def test_y_getter(self):
        r = Rectangle(15, 16, 0, 1)
        self.assertEqual(r.y, 1)
        
    def test_y_setter(self):
        r = Rectangle(15, 16, 0, 1)
        r.y = 3
        self.assertEqual(r.y, 3)















































































































if __name__ == '__main__':
    unittest.main()