import math

def biss(func, bounds, eps=1e-5):
    a, b = bounds
    if func(a) * func(b) > 0:
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
    return x ** 2  # math.sin(x), x**2-3, math.exp(x) - 6 * x - 3

x = biss(func, (-1, 3))

print('Полученный х = ', x, '\n', 'Значение функции в найденой точке: ', func(x), '\n')
