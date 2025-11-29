import math
import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        with self.assertRaises(ValueError):
            circle_area(0)

    def test_circle_area(self):
        res = circle_area(10)
        self.assertEqual(res, math.pi * 10 * 10)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            circle_area(-10)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            circle_perimeter(-10)

    def test_zero_perimeter(self):
        with self.assertRaises(ValueError):
            circle_perimeter(0)

    def test_correct_perimeter(self):
        res = circle_perimeter(10)
        self.assertEqual(res, math.pi * 2 * 10)

    def test_invalid_arg_area(self):
        with self.assertRaises(ValueError):
            circle_area("123")

    def test_float_perimeter(self):
        res = circle_perimeter(15.5)
        self.assertEqual(res, 15.5 * math.pi * 2)

    def test_invalid_arg_perimeter(self):
        with self.assertRaises(ValueError):
            circle_perimeter("304.2")


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        with self.assertRaises(ValueError):
            rectangle_area(10, 0)

    def test_square_area(self):
        res = rectangle_area(10, 10)
        self.assertEqual(res, 100)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            rectangle_area(-10, 1)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter(-10, 12)

    def test_zero_perimeter(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter(10, 0)

    def test_correct_perimeter(self):
        res = rectangle_perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_invalid_arg_area(self):
        with self.assertRaises(ValueError):
            rectangle_area("123", 20)

    def test_float_perimeter(self):
        res = rectangle_perimeter(15.5, 2)
        self.assertEqual(res, 35.0)


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        with self.assertRaises(ValueError):
            square_area(0)

    def test_square_area(self):
        res = square_area(10)
        self.assertEqual(res, 100)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            square_area(-10)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            square_perimeter(-10)

    def test_zero_perimeter(self):
        with self.assertRaises(ValueError):
            square_perimeter(0)

    def test_correct_perimeter(self):
        res = square_perimeter(10)
        self.assertEqual(res, 40)

    def test_invalid_arg_area(self):
        with self.assertRaises(ValueError):
            square_area("123")

    def test_float_perimeter(self):
        res = square_perimeter(15.33)
        self.assertAlmostEqual(res, 61.32, places=2)

    def test_invalid_arg_perimeter(self):
        with self.assertRaises(ValueError):
            square_perimeter("304.2")


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        with self.assertRaises(ValueError):
            triangle_area(0, 2, 4)

    def test_valid_sides_area(self):
        res = triangle_area(3, 4, 5)
        self.assertEqual(res, 6)

    def test_invalid_sides_area(self):
        with self.assertRaises(ValueError):
            triangle_area(3, 10, 5)

    def test_equilateral_triangle_area(self):
        res = triangle_area(10, 10, 10)
        self.assertAlmostEqual(res, 25 * math.sqrt(3), places=6)

    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            triangle_area(-10, 2, 3)

    def test_negative_sides_perimeter(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(-10, 42, -53)

    def test_float_perimeter(self):
        res = triangle_perimeter(2.5, 2.5, 5)
        self.assertEqual(res, 10)

    def test_correct_perimeter(self):
        res = triangle_perimeter(10, 5, 8)
        self.assertEqual(res, 23)

    def test_invalid_arg_area(self):
        with self.assertRaises(ValueError):
            triangle_area(20, 30, "slj")

    def test_valid_float_perimeter(self):
        res = triangle_perimeter(15.5, 14, 16.5)
        self.assertEqual(res, 46)

    def test_invalid_arg_perimeter(self):
        with self.assertRaises(ValueError):
            triangle_perimeter("30.2", 16.3, 18.8)

if __name__ == '__main__':
    unittest.main()