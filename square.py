import unittest


def area(a):
    '''Принимает число a, возвращает площадь квадрата со сторонами a
        Пример:
            area(2)
            Результат: 4
    '''
    if (type(a) == int) or (type(a) == float):
        if (a > 0):
            return a * a
        else:
            return ValueError
    else:
        return ValueError


def perimeter(a):
    '''Принимает число a, возвращает периметр квадрата со сторонами a
        Пример:
            perimeter(4)
            Результат: 16
    '''
    if (type(a) == int) or (type(a) == float):
        if (a > 0):
            return 4 * a
        else:
            return ValueError
    else:
        return ValueError



class SquareTestCase(unittest.TestCase):
    def test_zero(self):
        res = area(0)
        self.assertRaises(ValueError)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

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
        self.assertEqual(res, 40)

    def test_valid_arg_area(self):
        res = area("123")
        self.assertRaises(ValueError)

    def test_valid_arg_per(self):
        res = perimeter(15.33)
        self.assertEqual(res, 61.32)

    def test_invalid_arg_per(self):
        res = perimeter("304.2")
        self.assertRaises(ValueError)