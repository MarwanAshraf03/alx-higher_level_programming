#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Define unittests for testing of Square class"""

    def re(self):
        """Reset nb_instances to 0"""
        Base._Base__nb_objects = 0
        pass

    def test_instantiation_with_None(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square()

    def test_instantiation_with_size(self):
        """Doc"""
        r = Square(12)
        self.assertIsInstance(r, Square)

    def test_instantiation_with_size_wrong(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square('13')

    def test_instantiation_with_size_wrong2(self):
        """Doc"""
        with self.assertRaises(ValueError):
            r = Square(-1)

    def test_instantiation_with_size_wrong3(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(13.5)

    def test_instantiation_with_size_wrong4(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square((13.5, ))

    def test_instantiation_with_size_wrong5(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square([13.5])

    def test_instantiation_with_size_wrong6(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square({})

    def test_instantiation_with_x_wrong(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, "2", 5)

    def test_instantiation_with_x_wrong2(self):
        """Doc"""
        with self.assertRaises(ValueError):
            r = Square(12, -2, 5)

    def test_instantiation_with_x_wrong3(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, 2.5, 5)

    def test_instantiation_with_x_wrong4(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, (2, ), 5)

    def test_instantiation_with_x_wrong5(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, [2], 5)

    def test_instantiation_with_x_wrong6(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, {}, 5)

    def test_instantiation_with_y_wrong2(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, 5, "2")

    def test_instantiation_with_y_wrong3(self):
        """Doc"""
        with self.assertRaises(ValueError):
            r = Square(12, 5, -2)

    def test_instantiation_with_y_wrong4(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, 5, 2.5)

    def test_instantiation_with_y_wrong5(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, 5, (2, ))

    def test_instantiation_with_y_wrong(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, 5, [2])

    def test_instantiation_with_y_wrong6(self):
        """Doc"""
        with self.assertRaises(TypeError):
            r = Square(12, 5, {})

    def test_instantiation_with_size_and_height(self):
        """Doc"""
        r = Square(12)
        self.assertEqual(r.size, 12)

    def test_instantiation_full(self):
        """Doc"""
        r = Square(12, 0, 1, 14)
        self.assertEqual(r.size, 12)
        self.assertEqual(r.x, r.y - 1)
        self.assertEqual(r.id, 14)

    def test_size_getter(self):
        """Doc"""
        r = Square(15)
        self.assertEqual(r.size, 15)

    def test_size_setter(self):
        """Doc"""
        r = Square(15)
        r.size = 20
        self.assertEqual(r.size, 20)

    def test_x_getter(self):
        """Doc"""
        r = Square(15, 3, 1)
        self.assertEqual(r.x, 3)

    def test_x_setter(self):
        """Doc"""
        r = Square(15, 3, 1)
        r.x = 1
        self.assertEqual(r.x, 1)

    def test_y_getter(self):
        """Doc"""
        r = Square(15, 0, 1)
        self.assertEqual(r.y, 1)

    def test_y_setter(self):
        """Doc"""
        r = Square(15, 0, 1)
        r.y = 3
        self.assertEqual(r.y, 3)

    def test_area_1_arg(self):
        """Doc"""
        r = Square(10)
        with self.assertRaises(TypeError):
            r.area(23)

    def test_area(self):
        """Doc"""
        r = Square(10)
        self.assertEqual(r.area(), 100)

    def test_display(self):
        """Doc"""
        pass


if __name__ == '__main__':
    unittest.main()
