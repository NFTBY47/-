# Программа lab6_1
# Вычисление суммы по варианту 17
# Программист: Морозов А. П., гр. 444
# Проверил: Бурмистров А. С.
# Дата написания: 26.03.2025
# Переменные:
#   x0 - начальное значение x
#   hx - шаг
#   xn - конечное значение x
#   x - текущее значение аргумента
#   f - значение функции в точке x
#   f_max - максимальное значение функции
#   f_min - минимальное значение функции

print('Введите x0(hx)xn:')
x0 = float(input('x0 = '))
hx = float(input('hx = '))
xn = float(input('xn = '))

x = x0
# Вычисляем первое значение функции для инициализации
f_max = 4 * x**3 - 3 * x**2 + 2 * x - 1
f_min = f_max

while x <= xn + hx/2:  # Добавляем hx/2 для учета погрешности округления
    # Вычисляем значение функции в текущей точке
    f = 4 * x**3 - 3 * x**2 + 2 * x - 1
    
    # Обновляем максимальное и минимальное значения
    if f > f_max:
        f_max = f
    if f < f_min:
        f_min = f
    
    print('x = %.2f,\t f(x) = %8.4f' % (x, f))
    x += hx

distance = f_max - f_min
print('\nМаксимальное значение функции: %8.4f' % f_max)
print('Минимальное значение функции: %8.4f' % f_min)
print('Расстояние между max и min: %8.4f' % distance)