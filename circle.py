import math
import unittest


def area(r):
    '''Принимает чиcло r, возвращает площадь круга с радиусом r
        Пример:
            area(2)
            Результат: 12.566...
    '''
    if (type(r) == int) or (type(r) == float):
        if (r > 0):
            return math.pi * r * r
        else:
            return ValueError
    else:
        return ValueError


def perimeter(r):
    '''Принимает число r, возвращает длину окружности с радиусом r
        Пример:
            perimeter(4)
            Результат: 25.132...
    '''
    if (type(r) == int) or (type(r) == float):
        if (r > 0):
            return 2 * math.pi * r
        else:
            return ValueError
    else:
        return ValueError

class CircleTestCase(unittest.TestCase):
    def test_zero(self):
        res = area(0)
        self.assertRaises(ValueError)

    def test_circle_mul(self):
        res = area(10)
        self.assertEqual(res, math.pi * 10 * 10)

    def test_negative_area(self):
        res = area(-10)
        self.assertRaises(ValueError)

    def test_negative_per(self):
        res = perimeter(-10)
        self.assertRaises(ValueError)

    def test_per_nul(self):
        res = perimeter(0)
        self.assertRaises(ValueError)

    def test_correct_per(self):
        res = perimeter(10)
        self.assertEqual(res, math.pi * 2 * 10)

    def test_valid_arg_area(self):
        res = area("123")
        self.assertRaises(ValueError)

    def test_valid_arg_per(self):
        res = perimeter(15.5)
        self.assertEqual(res, 15.5 * math.pi * 2)

    def test_invalid_arg_per(self):
        res = perimeter("304.2")
        self.assertRaises(ValueError)