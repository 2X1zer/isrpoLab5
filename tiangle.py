import math

def area(a, b, c):
    ''' Принимает числа a,b,c возвращает площадь треугольника со сторонами a,b,c
        Пример:
            area(3,4,5)
            Результат: 6
    '''
    if ((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)) and ((type(c) == int) or (type(c) == float)):
        if (a + b >= c and a + c >= b and c + b >= a) and (a > 0 and b > 0 and c > 0):
            poluperimetr = perimeter(a, b, c) / 2
            return math.sqrt(poluperimetr * (poluperimetr - a) * (poluperimetr - b) * (poluperimetr - c))
        else:
            raise ValueError("Невалидные стороны треугольника")
    else:
        raise ValueError("Стороны должны быть числами")


def perimeter(a, b, c):
    ''' Принимает числа a,b,c возвращает периметр треугольника со сторонами a,b,c
        Пример:
            perimeter(4,3,2)
            Результат: 9
    '''
    if ((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)) and ((type(c) == int) or (type(c) == float)):
        if (a + b >= c and a + c >= b and c + b >= a) and (a > 0 and b > 0 and c > 0):
            return a + b + c
        else:
            raise ValueError("Невалидные стороны треугольника")
    else:
        raise ValueError("Стороны должны быть числами")