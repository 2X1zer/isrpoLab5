import math

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
            raise ValueError("Радиус должен быть положительным числом")
    else:
        raise ValueError("Радиус должен быть числом")


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
            raise ValueError("Радиус должен быть положительным числом")
    else:
        raise ValueError("Радиус должен быть числом")