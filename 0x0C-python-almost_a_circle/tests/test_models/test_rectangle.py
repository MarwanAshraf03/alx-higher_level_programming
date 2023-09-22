#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


class TestRectangle(unittest.TestCase):
    """Define unittests for testing of Rectangle class"""

    def re(self):
        """Reset nb_instances to 0"""
        Base._Base__nb_objects = 0
        pass

    def test_instantiation_with_None(self):
        """test instantiation with None"""
        with self.assertRaisesRegex(TypeError, ""):
            r = Rectangle()

    def test_instantiation_with_width(self):
        """test instantiation with width only"""
        with self.assertRaisesRegex(TypeError, ""):
            r = Rectangle(12)

    def test_instantiation_with_width_wrong(self):
        """test using string as width argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle('13', '12')

    def test_instantiation_with_width_wrong2(self):
        """test using value < 0 as width argument"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, '12')

    def test_instantiation_with_width_wrong3(self):
        """test using float value as width argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(13.5, '12')

    def test_instantiation_with_width_wrong4(self):
        """test using tuple value as width argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((13.5, ), '12')

    def test_instantiation_with_width_wrong5(self):
        """test using list value as width argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([13.5], '12')

    def test_instantiation_with_width_wrong6(self):
        """test using dictionary value as width argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({}, '12')

    def test_instantiation_with_width_wrong7(self):
        """test using 0 as width argument"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, '12')

    def test_instantiation_with_height_wrong(self):
        """test using string as height argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(12, '12')

    def test_instantiation_with_height_wrong2(self):
        """test using value < 0 as height argument"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(12, -1)

    def test_instantiation_with_height_wrong3(self):
        """test using float value as height argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(12, 13.5)

    def test_instantiation_with_height_wrong4(self):
        """test using tuple value as height argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(12, (13.5,))

    def test_instantiation_with_height_wrong5(self):
        """test using list value as height argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(12, [13.5])

    def test_instantiation_with_height_wrong6(self):
        """test using dictionary value as height argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(12, {})

    def test_instantiation_with_height_wrong7(self):
        """test using 0 as height argument"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(12, 0)

    def test_instantiation_with_x_wrong(self):
        """test using string as x argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(12, 15, "2", 5)

    def test_instantiation_with_x_wrong2(self):
        """test using value < 0 as x argument"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(12, 15, -2, 5)

    def test_instantiation_with_x_wrong3(self):
        """test using float value as x argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(12, 15, 2.5, 5)

    def test_instantiation_with_x_wrong4(self):
        """test using tuple value as x argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(12, 15, (2, ), 5)

    def test_instantiation_with_x_wrong5(self):
        """test using list value as x argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(12, 15, [2], 5)

    def test_instantiation_with_x_wrong6(self):
        """test using dictionary value as x argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(12, 15, {}, 5)

    def test_instantiation_with_y_wrong(self):
        """test using list value as y argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(12, 15, 5, [2])

    def test_instantiation_with_y_wrong2(self):
        """test using string as y argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(12, 15, 5, "2")

    def test_instantiation_with_y_wrong3(self):
        """test using value < 0 as y argument"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(12, 15, 5, -2)

    def test_instantiation_with_y_wrong4(self):
        """test using float value as y argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(12, 15, 5, 2.5)

    def test_instantiation_with_y_wrong5(self):
        """test using tuple value as y argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(12, 15, 5, (2, ))

    def test_instantiation_with_y_wrong6(self):
        """test using dictionary value as y argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(12, 15, 5, {})

    def test_instantiation_with_width_and_height(self):
        """test using only width and height as arguments"""
        r = Rectangle(12, 13)
        self.assertEqual(r.width, r.height - 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_instantiation_full(self):
        """test using width, height, x, y and id"""
        r = Rectangle(12, 13, 0, 1, 14)
        self.assertEqual(r.width, r.height - 1)
        self.assertEqual(r.x, r.y - 1)
        self.assertEqual(r.id, 14)

    def test_width_getter(self):
        """test width getter"""
        r = Rectangle(15, 16)
        self.assertEqual(r.width, 15)

    def test_width_setter(self):
        """test width setter"""
        r = Rectangle(15, 16)
        r.width = 20
        self.assertEqual(r.width, 20)

    def test_height_getter(self):
        """test height getter"""
        r = Rectangle(15, 16)
        self.assertEqual(r.height, 16)

    def test_height_setter(self):
        """test height setter"""
        r = Rectangle(15, 16)
        r.height = 20
        self.assertEqual(r.height, 20)

    def test_x_getter(self):
        """test x getter"""
        r = Rectangle(15, 16, 3, 1)
        self.assertEqual(r.x, 3)

    def test_x_setter(self):
        """test x setter"""
        r = Rectangle(15, 16, 3, 1)
        r.x = 1
        self.assertEqual(r.x, 1)

    def test_y_getter(self):
        """test y getter"""
        r = Rectangle(15, 16, 0, 1)
        self.assertEqual(r.y, 1)

    def test_y_setter(self):
        """test y setter"""
        r = Rectangle(15, 16, 0, 1)
        r.y = 3
        self.assertEqual(r.y, 3)

    def test_area_1_arg(self):
        """test using area method with 1 argument"""
        r = Rectangle(10, 15)
        with self.assertRaises(TypeError):
            r.area(23)

    def test_area(self):
        """test using area method the right way"""
        r = Rectangle(10, 15)
        self.assertEqual(r.area(), 150)

    def test_display_with_arg(self):
        """test using display method with an argument"""
        r = Rectangle(4, 3)
        with self.assertRaises(TypeError):
            r.display(5)

    def test_display(self):
        """test using display method with no x or y"""
        r = Rectangle(4, 3)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "####\n####\n####\n")

    def test_display2(self):
        """test using display method with no x or y second time"""
        r = Rectangle(5, 2)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "#####\n#####\n")

    def test_display_x(self):
        """test using display method with x = 2, y = 0"""
        r = Rectangle(4, 3, 2)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "  ####\n  ####\n  ####\n")

    def test_display_y(self):
        """test using display method with x = 0, y = 2"""
        r = Rectangle(4, 3, 0, 2)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "\n\n####\n####\n####\n")

    def test_display_x_y(self):
        """test using display method with x = 2, y = 3"""
        r = Rectangle(4, 3, 2, 3)
        capOut = io.StringIO()
        sys.stdout = capOut
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capOut.getvalue(), "\n\n\n  ####\n  ####\n  ####\n")

    def test_str_(self):
        """test __str__ method"""
        self.re()
        r = Rectangle(12, 14)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 0/0 - 12/14")

    def test_to_dictionary(self):
        """test using to_dictionary method"""
        r = Rectangle(12, 14)
        self.assertEqual(
            r.to_dictionary(), {
                'x': 0, 'width': 12, 'id': 2, 'height': 14, 'y': 0
                })

    def test_to_json_string(self):
        """test to_json_string method"""
        self.re()
        r = Rectangle(1, 2, 3, 4)
        r1 = Rectangle(2, 2, 3, 4)
        json_str = Base.to_json_string([r.to_dictionary(), r1.to_dictionary()])
        self.assertEqual(
            json_str,
            '[{"x": 3, "width": 1, "id": 1, "height": 2, "y": 4},' +
            ' {"x": 3, "width": 2, "id": 2, "height": 2, "y": 4}]'
              )

    def test_update(self):
        """test using update method for *args"""
        r = Rectangle(12, 14)
        r.update(12, 13, 15, 15, 6)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 6)

    def test_update2(self):
        """test using update method for **kwargs"""
        r = Rectangle(12, 14)
        r.update(id=12, width=13, height=15, x=15, y=6)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 6)

    def test_update3(self):
        """test using update method for both *args and **kwargs are given"""
        r = Rectangle(12, 14)
        r.update(12, 13, 15, 15, 6, id=12, width=13, height=15, x=15, y=6)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 6)

    def test_create(self):
        """test using create method with id only"""
        r = Rectangle(1, 2)
        r1 = r.create(**{"id": 1})
        self.assertIsInstance(r1, Rectangle)

    def test_create2(self):
        """test using create method with id and width"""
        r = Rectangle(1, 2)
        r1 = r.create(**{"id": 1, "width": 2})
        self.assertIsInstance(r1, Rectangle)

    def test_create3(self):
        """test using create method with id, width and height"""
        r = Rectangle(1, 2)
        r1 = r.create(**{"id": 1, "width": 2, "height": 3})
        self.assertIsInstance(r1, Rectangle)

    def test_create4(self):
        """test using create method with id, width, height and x"""
        r = Rectangle(1, 2)
        r1 = r.create(**{"id": 1, "width": 2, "height": 3, "x": 1})
        self.assertIsInstance(r1, Rectangle)

    def test_create5(self):
        """test using create method with id, width, height, x and y"""
        r = Rectangle(1, 2)
        r1 = r.create(**{"id": 1, "width": 2, "height": 3, "x": 1, "y": 2})
        self.assertIsInstance(r1, Rectangle)

    def test_save_to_file(self):
        """test using save_to_file method with 2 instances"""
        self.re()
        r = Rectangle(1, 3)
        r1 = Rectangle(2, 3)
        Rectangle.save_to_file([r, r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                f.read(),
                '[{"x": 0, "width": 1, "id": 1, "height": 3, "y": 0},' +
                ' {"x": 0, "width": 2, "id": 2, "height": 3, "y": 0}]')

    def test_save_to_file2(self):
        """test using save_to_file method with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file3(self):
        """test using save_to_file method with one instance"""
        self.re()
        r = Rectangle(1, 3)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                f.read(),
                '[{"x": 0, "width": 1, "id": 1, "height": 3, "y": 0}]')

    def test_save_to_file4(self):
        """test using save_to_file method with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file(self):
        """test using load_from_file method"""
        self.re()
        r = Rectangle(1, 3)
        Rectangle.save_to_file([r])
        r1 = Rectangle.load_from_file()
        self.assertEqual(r.id, r1[0].id)
        self.assertEqual(r.width, r1[0].width)
        self.assertEqual(r.height, r1[0].height)
        self.assertEqual(r.x, r1[0].x)
        self.assertEqual(r.y, r1[0].y)
        self.assertNotEqual(r.__str__, r1[0].__str__)


if __name__ == '__main__':
    unittest.main()
