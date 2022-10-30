import math
from scipy.misc import derivative

def biss(func, bounds, eps=1e-5):
    a, b = bounds
    if func(a) * func(b) > 0:
        x1 = -3
        if (proizv(0) == 0):
            print('Полученный х = ', proizv(0), '\n', 'Значение функции в найденой точке: ', proizv(0), '\n')
            exit(0)
        elif (func(x1) == 0):
            print('Полученный х = ', x1, '\n', 'Значение функции в найденой точке: ', func(x1), '\n')
            exit(0)
        else:
            print('На заданном интервале нет корней')
            exit(0)
    x0 = (a + b) / 2
    while abs(a - b) >= eps:
        if func(a) * func(x0) > 0:
            a = x0
        else:
            b = x0
        x0 = (a + b) / 2
    return x0


def func(x):
    return x ** 2  # math.sin(x) (-1, 3), -x ** 2 + 4 (-2, 5), math.exp(x) - 6 * x - 3 (-6, 3), (x + 3) ** 2, x ** 2
def proizv(x):
    return derivative(func, x)

x = biss(func, (-6, 3))

print('Полученный х = ', x, '\n', 'Значение функции в найденой точке: ', func(x), '\n')
