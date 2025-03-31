# lab 10
# Матрицы
# Дата написания: 03.03.2025
# Програмист: Морозов А. П.
# Проверил: Бурмистров А. С. 
# Переменные:
    # a - Матрица
    # n, m - Число строк, число столбцов
    # i, j - Параметры цикла
    # amin - минимальный элемент 
    # imin, jmin - индексы минимума

# Ввод матрицы с клавиатуры
n = int(input("Введите число строк в матрице: "))
m = int(input("Введите число столбцов в матрие: "))
a = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        print(f'a[{i}], [{j}] = ', end='')
        a[i][j] = int(input())

#print(a)
#Вывод матрицы: 
print("Исходная матрица")
for i in range(n):
    for j in range(m):
        print(a[i][j], end='\t')
    print()

# Поиск и вывод минимального элемента: 
amin = a[0][0]
imin = 0
jmin = 0
for i in range(n):
    for j in range(m):    
        if a[i][j] < amin:
            amin = a[i][j]
            imin = i
            jmin = j
print(f"Минимальный элемент = {amin}, в диапозоне {imin}, {jmin}")

#Обнуление правее и ниже данного элемента
for i in range(imin, n):
    a[i][jmin] = 0
    
for j in range(jmin, m):
        a[imin][j] = 0
a[imin][jmin] = amin
#Вывод измененной матрицы
print("\nМатрица после обнуления элементов ниже и правее минимального:")
for i in range(n):
    for j in range(m):
        print(a[i][j], end='\t')
    print()
