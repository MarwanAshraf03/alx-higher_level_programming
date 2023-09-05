#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer()"""

    def test_noArgs(self):
        """Test for no arguments"""
        self.assertEqual(max_integer(), None)

    def test_emptyList(self):
        """Test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_oneElementInList(self):
        """Test for list with 1 item"""
        self.assertEqual(max_integer([1]), 1)

    def test_twoRepeatedElements(self):
        """Test for repeated items"""
        self.assertEqual(max_integer([1, 2, 2]), 2)

    def test_negativeNumbers(self):
        """Test for negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_tupleOneElement(self):
        """Test for one element tuple"""
        self.assertEqual(max_integer((2, )), 2)

    def test_tupleMultipleElements(self):
        """Test for many tuple elements"""
        self.assertEqual(max_integer((2, 4)), 4)

    def test_string(self):
        """Test for string"""
        self.assertEqual(max_integer("True"), "u")

    def test_oneStringList(self):
        """Test for string"""
        self.assertEqual(max_integer(["True"]), "True")

    def test_stringList(self):
        """Test for list of strings"""
        self.assertEqual(max_integer(["True", "False", "School"]), "True")

    def test_wrongArgs(self):
        """Test for wrongs items"""
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, 2, 3)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 2j)
        self.assertRaises(TypeError, max_integer, [True, "True", 3.5, 2])

    def test_intAndFloatitems(self):
        """Test for integer and float items"""
        self.assertEqual(max_integer([1, 3.9, 3.5, 2]), 3.9)

    def test_tooManyIntegerItems(self):
        """Test for many integer items"""
        self.assertEqual(max_integer([
            1000, 1010, 1020, 1030, 1040,
            1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500,
            1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610,
            1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720,
            1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830,
            1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940,
            1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050,
            2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160
            ]), 2160)

    def test_tooManyIntegersAndFloatItems(self):
        """Test for many integer and float items"""
        self.assertEqual(max_integer([
            1000, 1100, 1200, 1300, 1400,
            1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500,
            2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600,
            3700, 3800, 3900, 4000,
            41000.6, 4200, 4300, 4400, 4500, 4600, 4700,
            4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800,
            5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900
            ]), 41000.6)


if __name__ == '__main__':
    unittest.main()
