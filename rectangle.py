import unittest

def area(a,b):
    ''' Принимает числа a,b возвращает площадь прямоугольника со сторонами a,b
        Пример:
            area(2,3)
            Результат: 6
    '''
    if (((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float))):
        if (a > 0 and b > 0):
            return a * b
        else:
            return ValueError
    else:
        return ValueError


def perimeter(a,b):
    ''' Принимает числа a,b возвращает периметр прямоугольника со сторонами a,b
        Пример:
            perimeter(4,3)
            Результат: 14
    '''
    if (((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float))):
        if (a > 0 and b > 0):
            return 2 * a + 2 * b
        else:
            return ValueError
    else:
        return ValueError


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertRaises(ValueError)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_negative_area(self):
        res = area(-10,1)
        self.assertRaises(ValueError)

    def test_negative_per(self):
        res = perimeter(-10,12)
        self.assertRaises(ValueError)

    def test_per_nul(self):
        res = perimeter(10, 0)
        self.assertRaises(ValueError)

    def test_correct_per(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_valid_arg_area(self):
        res = area("123",20)
        self.assertRaises(ValueError)

    def test_valid_arg_per(self):
        res = perimeter(15.5, 2)
        self.assertEqual(res, 35.0)