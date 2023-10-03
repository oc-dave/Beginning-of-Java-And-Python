import unittest
from radius import area
from math import pi


class Test_Area(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2), pi * 2 ** 2)

    def test_that_values_function(self):
        self.assertRaises()


if __name__ == '__main__':
    unittest.main()
