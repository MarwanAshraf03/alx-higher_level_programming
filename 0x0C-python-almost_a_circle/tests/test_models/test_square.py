#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import io
import sys


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

    def test_instantiation_with_size(self):
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

    def test_display_with_arg(self):
        """test using display method with an argument"""
        r = Square(4)
        with self.assertRaises(TypeError):
            r.display(5)

    def test_display(self):
        """test using display method the right way"""
        r = Square(4)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "####\n####\n####\n####\n")

    def test_display2(self):
        """test using display method the right way"""
        r = Square(5)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            capOut.getvalue(),
            "#####\n#####\n#####\n#####\n#####\n")

    def test_display_x_err(self):
        """test using display method the error way"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(4, -2)

    def test_display_y_err(self):
        """test using display method the error way"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(4, 0, -2)

    def test_display_x(self):
        """test using display method the right way"""
        r = Square(4, 2)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "  ####\n  ####\n  ####\n  ####\n")

    def test_display_y(self):
        """test using display method the right way"""
        r = Square(4, 0, 2)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "\n\n####\n####\n####\n####\n")

    def test_display_x_y(self):
        """test using display method the right way"""
        r = Square(4, 2, 3)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            capOut.getvalue(),
            "\n\n\n  ####\n  ####\n  ####\n  ####\n")

    def test_str_(self):
        self.re()
        r = Square(12)
        self.assertEqual(r.__str__(), "[Square] (1) 0/0 - 12")

    def test_to_dictionary(self):
        """test using to_dictionary method"""
        r = Square(12)
        self.assertEqual(
            r.to_dictionary(), {'id': 2, 'size': 12, 'x': 0, 'y': 0})

    def test_to_json_string(self):
        self.re()
        r = Square(1, 3, 4)
        r1 = Square(2, 3, 4)
        json_str = Base.to_json_string([r.to_dictionary(), r1.to_dictionary()])
        self.assertEqual(
            json_str,
            '[{"id": 1, "size": 1, "x": 3, "y": 4}, ' +
            '{"id": 2, "size": 2, "x": 3, "y": 4}]')

    def test_update(self):
        """test using update method for *args"""
        r = Square(12)
        r.update(12, 15, 15, 6)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.size, 15)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 6)

    def test_update2(self):
        """test using update method for **kwargs"""
        r = Square(12)
        r.update(id=12, size=15, x=15, y=6)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.size, 15)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 6)

    def test_update3(self):
        """test using update method for both *args and **kwargs are given"""
        r = Square(12, 14)
        r.update(12, 15, 15, 6, id=12, size=13, height=15, x=15, y=6)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.size, 15)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 6)

    def test_create(self):
        """test using create method"""
        r = Square(1, 2)
        r1 = r.create(**{"id": 1})
        self.assertIsInstance(r1, Square)

    def test_create2(self):
        """test using create method"""
        r = Square(1, 2)
        r1 = r.create(**{"id": 1, "size": 2})
        self.assertIsInstance(r1, Square)

    def test_create3(self):
        """test using create method"""
        r = Square(1, 2)
        r1 = r.create(**{"id": 1, "size": 2, "height": 3, "x": 1})
        self.assertIsInstance(r1, Square)

    def test_create4(self):
        """test using create method"""
        r = Square(1, 2)
        r1 = r.create(**{"id": 1, "size": 2, "height": 3, "x": 1, "y": 2})
        self.assertIsInstance(r1, Square)

    def test_save_to_file(self):
        """test using save_to_file method"""
        self.re()
        r = Square(1, 3)
        r1 = Square(2, 3)
        Square.save_to_file([r, r1])
        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(),
                '[{"id": 1, "size": 1, "x": 3, "y": 0}, ' +
                '{"id": 2, "size": 2, "x": 3, "y": 0}]')

    def test_save_to_file2(self):
        """test using save_to_file method"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file3(self):
        """test using save_to_file method"""
        self.re()
        r = Square(1, 3)
        Square.save_to_file([r])
        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(),
                '[{"id": 1, "size": 1, "x": 3, "y": 0}]')

    def test_load_from_file_true(self):
        """test using save_to_file method"""
        self.re()
        r = Square(1, 3)
        Square.save_to_file([r])
        r1 = Square.load_from_file()
        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(),
                '[{"id": 1, "size": 1, "x": 3, "y": 0}]')


if __name__ == '__main__':
    unittest.main()
