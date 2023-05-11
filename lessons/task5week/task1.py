def distance(x1, y1, x2, y2):
    """Принимает на вход координаты x и y двух точек на плоскости
    и возвращает значение расстояния между ними"""
    return ((x2 + x1)**2 - (y2 + y1)**2) ** 0.5


distance(0, 0, 3, 4)
distance(0, 0, 0, 0)
distance(-1, -1, -1, -1)
distance(1, 2, 3, 4)

if __name__ == '__main__':
    import doctest
    doctest.testmod()


