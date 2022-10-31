import math
import sys

def biss(func, bounds, eps=1e-5):
    a, b = bounds
    if func(a) * func(b) > 0:
        x0 = biss(proizv, bounds)
        if (math.isnan(x0)):
            print('Корней нет на интервале')
            exit(0)
        return x0
    x0 = (a + b) / 2
    while abs(a - b) >= eps:
        if func(a) * func(x0) > 0:
            a = x0
        else:
            b = x0
        x0 = (a + b) / 2
    return x0


def func(x):
    return math.sin(x)+math.cos(x)
#math.sin(x**2) (-4.2, 12) math.sin(x)+math.cos(x) (-5, 6) ln(x+2) x**2 (-4.2, 12) (x-3)**2 (-1, 3)

def proizv(x):
    return math.cos(x)-math.sin(x)

x = biss(func, (-5, 6))

print('Полученный х = ', x, '\n', 'Значение функции в найденой точке: ', func(x), '\n')
