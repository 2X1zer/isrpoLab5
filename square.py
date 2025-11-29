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
            raise ValueError("Сторона должна быть положительным числом")
    else:
        raise ValueError("Сторона должна быть числом")


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
            raise ValueError("Сторона должна быть положительным числом")
    else:
        raise ValueError("Сторона должна быть числом")