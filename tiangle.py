import math
import unittest


def area(a,b,c):
    ''' Принимает числа a,b,c возвращает площадь треугольника со сторонами a,b,c
        Пример:
            area(3,4,5)
            Результат: 6
    '''
    if ((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)) and ((type(c) == int) or (type(c) == float)):
        if (a + b >= c and a + c >= b and c + b >= a) and (a >= 0 and b >= 0 and c >= 0):
            poluperimetr = perimeter(a,b,c)/2
            return math.sqrt(poluperimetr*(poluperimetr - a)*(poluperimetr - b)*(poluperimetr - c))
        else:
            return ValueError
    else:
        return ValueError


def perimeter(a,b,c):
    ''' Принимает числа a,b,c возвращает периметр треугольника со сторонами a,b,c
        Пример:
            perimeter(4,3,2)
            Результат: 9
    '''
    if ((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)) and ((type(c) == int) or (type(c) == float)):
        if (a + b >= c and a + c >= b and c + b >= a) and (a >= 0 and b >= 0 and c >= 0):
            return a+b+c
        else:
            return ValueError
    else:
        return ValueError


class TriangleTestCase(unittest.TestCase):
    def test_zero(self):
        res = area(0, 2, 4)
        self.assertRaises(ValueError)

    def test_valid_sides(self):
        res = area(3, 4, 5)
        self.assertEqual(res, 6)

    def test_invalid_sides(self):
        res = area(3, 10, 5)
        self.assertRaises(ValueError)

    def test_triangle_mul(self):
        res = area(10, 10, 10)
        self.assertEqual(res, 25*3**0.5)

    def test_negative_side(self):
        res = area(-10,2,3)
        self.assertRaises(ValueError)

    def test_negative_per_side(self):
        res = perimeter(-10,42,-53)
        self.assertRaises(ValueError)

    def test_per_side(self):
        res = perimeter(2.5,2.5,5)
        self.assertEqual(res, 10)

    def test_correct_per(self):
        res = perimeter(10,5,8)
        self.assertEqual(res, 23)

    def test_invalid_arg_area(self):
        res = area(20, 30, "slj")
        self.assertRaises(ValueError)

    def test_valid_arg(self):
        res = perimeter(15.5, 14,16.5)
        self.assertEqual(res, 46)

    def test_invalid_arg_per(self):
        res = perimeter("30.2",16.3, 18.8)
        self.assertRaises(ValueError)