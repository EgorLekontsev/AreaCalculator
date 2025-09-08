import unittest
from area_calculator import Circle, Triangle, Square
from math import pi

class TestCircle(unittest.TestCase):
    def test_area_radius_one(self):
        c = Circle(1.0)
        self.assertAlmostEqual(c.area(), pi)


class TestTriangle(unittest.TestCase):
    def test_area_3_4_5(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0)

    def test_is_right_true(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right())

    def test_is_right_false(self):
        t = Triangle(2, 3, 4)
        self.assertFalse(t.is_right())


class TestSquare(unittest.TestCase):
    def test_area_square(self):
        s = Square(2.0)
        self.assertAlmostEqual(s.area(), 4.0)


if __name__ == '__main__':
    unittest.main()
