def area(a, b):
    ''' Принимает числа a,b возвращает площадь прямоугольника со сторонами a,b
        Пример:
            area(2,3)
            Результат: 6
    '''
    if (((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float))):
        if (a > 0 and b > 0):
            return a * b
        else:
            raise ValueError("Стороны должны быть положительными числами")
    else:
        raise ValueError("Стороны должны быть числами")


def perimeter(a, b):
    ''' Принимает числа a,b возвращает периметр прямоугольника со сторонами a,b
        Пример:
            perimeter(4,3)
            Результат: 14
    '''
    if (((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float))):
        if (a > 0 and b > 0):
            return 2 * a + 2 * b
        else:
            raise ValueError("Стороны должны быть положительными числами")
    else:
        raise ValueError("Стороны должны быть числами")