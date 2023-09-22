#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.base import Base
from models.square import Square
import io
import sys


class TestSquare(unittest.TestCase):
    """Define unittests for testing of Square class"""

    def re(self):
        """Reset nb_instances to 0"""
        Base._Base__nb_objects = 0
        pass

    def test_instantiation_with_None(self):
        """test instantiation with None"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_instantiation_with_zero(self):
        """test instantiation with 0 as size"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_instantiation_with_normal(self):
        """test normal instantiation"""
        s = Square(12)
        self.assertIsInstance(s, Square)

    def test_instantiation_with_size_wrong(self):
        """test using string as size argument"""
        with self.assertRaises(TypeError):
            s = Square('13')

    def test_instantiation_with_size_wrong2(self):
        """test using value < 0 as size argument"""
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_instantiation_with_size_wrong3(self):
        """test using float as size argument"""
        with self.assertRaises(TypeError):
            s = Square(13.5)

    def test_instantiation_with_size_wrong4(self):
        """test using tuple as size argument"""
        with self.assertRaises(TypeError):
            s = Square((13.5, ))

    def test_instantiation_with_size_wrong5(self):
        """test using list as size argument"""
        with self.assertRaises(TypeError):
            s = Square([13.5])

    def test_instantiation_with_size_wrong6(self):
        """test using dictionary as size argument"""
        with self.assertRaises(TypeError):
            s = Square({})

    def test_instantiation_with_x_wrong(self):
        """test using string as x argument"""
        with self.assertRaises(TypeError):
            s = Square(12, "2", 5)

    def test_instantiation_with_x_wrong2(self):
        """test using value < 0 as x argument"""
        with self.assertRaises(ValueError):
            s = Square(12, -2, 5)

    def test_instantiation_with_x_wrong3(self):
        """test using float value as x argument"""
        with self.assertRaises(TypeError):
            s = Square(12, 2.5, 5)

    def test_instantiation_with_x_wrong4(self):
        """test using tuple value as x argument"""
        with self.assertRaises(TypeError):
            s = Square(12, (2, ), 5)

    def test_instantiation_with_x_wrong5(self):
        """test using list value as x argument"""
        with self.assertRaises(TypeError):
            s = Square(12, [2], 5)

    def test_instantiation_with_x_wrong6(self):
        """test using dictionary value as x argument"""
        with self.assertRaises(TypeError):
            s = Square(12, {}, 5)

    def test_instantiation_with_y_wrong(self):
        """test using list value as y argument"""
        with self.assertRaises(TypeError):
            s = Square(12, 5, [2])

    def test_instantiation_with_y_wrong2(self):
        """test using string as y argument"""
        with self.assertRaises(TypeError):
            s = Square(12, 5, "2")

    def test_instantiation_with_y_wrong3(self):
        """test using value < 0 as y argument"""
        with self.assertRaises(ValueError):
            s = Square(12, 5, -2)

    def test_instantiation_with_y_wrong4(self):
        """test using float value as y argument"""
        with self.assertRaises(TypeError):
            s = Square(12, 5, 2.5)

    def test_instantiation_with_y_wrong5(self):
        """test using tuple value as y argument"""
        with self.assertRaises(TypeError):
            s = Square(12, 5, (2, ))

    def test_instantiation_with_y_wrong6(self):
        """test using dictionary value as y argument"""
        with self.assertRaises(TypeError):
            s = Square(12, 5, {})

    def test_instantiation_with_size(self):
        """test instantiation with size only"""
        s = Square(12)
        self.assertEqual(s.size, 12)

    def test_instantiation_full(self):
        """test instantiation with all arguments"""
        s = Square(12, 0, 1, 14)
        self.assertEqual(s.size, 12)
        self.assertEqual(s.x, s.y - 1)
        self.assertEqual(s.id, 14)

    def test_size_getter(self):
        """test size getter"""
        s = Square(15)
        self.assertEqual(s.size, 15)

    def test_size_setter(self):
        """test size setter"""
        s = Square(15)
        s.size = 20
        self.assertEqual(s.size, 20)

    def test_x_getter(self):
        """test x getter"""
        s = Square(15, 3, 1)
        self.assertEqual(s.x, 3)

    def test_x_setter(self):
        """test x setter"""
        s = Square(15, 3, 1)
        s.x = 1
        self.assertEqual(s.x, 1)

    def test_y_getter(self):
        """test y getter"""
        s = Square(15, 0, 1)
        self.assertEqual(s.y, 1)

    def test_y_setter(self):
        """test y setter"""
        s = Square(15, 0, 1)
        s.y = 3
        self.assertEqual(s.y, 3)

    def test_area_1_arg(self):
        """test using area method with 1 argument"""
        s = Square(10)
        with self.assertRaises(TypeError):
            s.area(23)

    def test_area(self):
        """test using area method the right way"""
        s = Square(10)
        self.assertEqual(s.area(), 100)

    def test_display_with_arg(self):
        """test using display method with an argument"""
        s = Square(4)
        with self.assertRaises(TypeError):
            s.display(5)

    def test_display(self):
        """test using display method with no x or y"""
        s = Square(4)
        capOut = io.StringIO()
        sys.stdout = capOut
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "####\n####\n####\n####\n")

    def test_display2(self):
        """test using display method with no x or y second time"""
        s = Square(5)
        capOut = io.StringIO()
        sys.stdout = capOut
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            capOut.getvalue(),
            "#####\n#####\n#####\n#####\n#####\n")

    def test_display_x(self):
        """test using display method with x = 2, y = 0"""
        s = Square(4, 2)
        capOut = io.StringIO()
        sys.stdout = capOut
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "  ####\n  ####\n  ####\n  ####\n")

    def test_display_y(self):
        """test using display method with x = 0, y = 2"""
        s = Square(4, 0, 2)
        capOut = io.StringIO()
        sys.stdout = capOut
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "\n\n####\n####\n####\n####\n")

    def test_display_x_y(self):
        """test using display method with x = 2, y = 3"""
        s = Square(4, 2, 3)
        capOut = io.StringIO()
        sys.stdout = capOut
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            capOut.getvalue(),
            "\n\n\n  ####\n  ####\n  ####\n  ####\n")

    def test_str_(self):
        """test __str__ method"""
        self.re()
        s = Square(12)
        self.assertEqual(s.__str__(), "[Square] (1) 0/0 - 12")

    def test_to_dictionary(self):
        """test using to_dictionary method"""
        s = Square(12)
        self.assertEqual(
            s.to_dictionary(), {'id': 2, 'size': 12, 'x': 0, 'y': 0})

    def test_to_json_string(self):
        """test to_json_string method"""
        self.re()
        s = Square(1, 3, 4)
        s1 = Square(2, 3, 4)
        json_str = Base.to_json_string([s.to_dictionary(), s1.to_dictionary()])
        self.assertEqual(
            json_str,
            '[{"id": 1, "size": 1, "x": 3, "y": 4}, ' +
            '{"id": 2, "size": 2, "x": 3, "y": 4}]')

    def test_update(self):
        """test using update method for *args"""
        s = Square(12)
        s.update(12, 15, 15, 6)
        self.assertEqual(s.id, 12)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 15)
        self.assertEqual(s.y, 6)

    def test_update2(self):
        """test using update method for **kwargs"""
        s = Square(12)
        s.update(id=12, size=15, x=15, y=6)
        self.assertEqual(s.id, 12)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 15)
        self.assertEqual(s.y, 6)

    def test_update3(self):
        """test using update method for both *args and **kwargs are given"""
        s = Square(12, 14)
        s.update(12, 15, 15, 6, id=12, size=13, height=15, x=15, y=6)
        self.assertEqual(s.id, 12)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 15)
        self.assertEqual(s.y, 6)

    def test_create(self):
        """test using create method with id only"""
        s = Square(1, 2)
        s1 = s.create(**{"id": 1})
        self.assertIsInstance(s1, Square)

    def test_create2(self):
        """test using create method with id and size"""
        s = Square(1, 2)
        s1 = s.create(**{"id": 1, "size": 2})
        self.assertIsInstance(s1, Square)

    def test_create3(self):
        """test using create method with id, size and x"""
        s = Square(1, 2)
        s1 = s.create(**{"id": 1, "size": 2, "x": 1})
        self.assertIsInstance(s1, Square)

    def test_create4(self):
        """test using create method with id, size, x and y"""
        s = Square(1, 2)
        s1 = s.create(**{"id": 1, "size": 2, "x": 1, "y": 2})
        self.assertIsInstance(s1, Square)

    def test_save_to_file(self):
        """test using save_to_file method with 2 instances"""
        self.re()
        s = Square(1, 3)
        s1 = Square(2, 3)
        Square.save_to_file([s, s1])
        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(),
                '[{"id": 1, "size": 1, "x": 3, "y": 0}, ' +
                '{"id": 2, "size": 2, "x": 3, "y": 0}]')

    def test_save_to_file2(self):
        """test using save_to_file method with empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file3(self):
        """test using save_to_file method with one instance"""
        self.re()
        s = Square(1, 3)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(),
                '[{"id": 1, "size": 1, "x": 3, "y": 0}]')

    def test_save_to_file4(self):
        """test using save_to_file method with None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file(self):
        """test using load_from_file method"""
        self.re()
        s = Square(3)
        Square.save_to_file([s])
        s1 = Square.load_from_file()
        self.assertEqual(s.id, s1[0].id)
        self.assertEqual(s.size, s1[0].size)
        self.assertEqual(s.x, s1[0].x)
        self.assertEqual(s.y, s1[0].y)
        self.assertNotEqual(s.__str__, s1[0].__str__)


if __name__ == '__main__':
    unittest.main()
