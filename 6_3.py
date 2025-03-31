  yyy
# Переменные:
#   x0 - начальное значение x
#   hx - шаг изменения x
#   xn - конечное значение x
#   nx - количество шагов
#   i - параметр цикла
#   s - сумма значений функции
#   p - произведение значений функции
#   y - значение функции в точке x

from math import trunc, sin, cos, fabs, pow

print('Введите x = x0(hx)xn')
x0 = float(input('x0 = '))
hx = float(input('hx = '))
xn = float(input('xn = '))

s = 0
p = 1
x = x0
nx = trunc((xn - x0) / hx + 1E-6) + 1

for i in range(nx):
    if x < 1:
        y = float('nan')  # Функция не определена
    elif 1 <= x <= 3:
        y = (x / 2) * pow(fabs(1 + x), 1/3)
    elif x > 3:
        y = sin(2 * x)
    else:
        y = 2 + cos(3 * x)  # Эта ветка по условию не достигается
    
    if not isinstance(y, float) or y != y:  # Проверка на NaN
        print('x = %.2f\tфункция не определена' % x)
    else:
        s += y
        p *= y
        print('x = %.2f\ty = %.6f' % (x, y))
    x += hx

print('Сумма всех y = %.6f' % s)
print('Произведение всех y = %.6f' % p)