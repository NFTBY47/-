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
#   s - результат вычисления
#   n, k - параметры циклов
#   numerator, denominator - числитель и знаменатель
#   power - степень числа (вычисляется через цикл)

print('Введите x = x0(hx)xn')
x0 = float(input('x0 = '))
hx = float(input('hx = '))
xn = float(input('xn = '))

x = x0
while x <= xn + hx/2:  
    if x <= 0.5:
        # Вычисляем сумму для x ≤ 0.5: sum(n=1 to 8) (n*x)/(n*x^2 + 1)
        s = 0
        for n in range(1, 9):
            # Вычисляем x^2 через цикл
            x_squared = 1
            for _ in range(2):
                x_squared *= x
            
            denominator = n * x_squared + 1
            term = (n * x) / denominator
            s += term
    else:
        # Вычисляем сумму для x > 0.5: sum(k=0 to 8) (x^k)/(k+1)
        s = 0
        for k in range(0, 9):
            # Вычисляем x^k через цикл
            power = 1
            for _ in range(k):
                power *= x
            
            term = power / (k + 1)
            s += term
    
    print('x = %.2f\ts = %.6f' % (x, s))
    x += hx