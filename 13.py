import random

CONST_D = 100  # Константа для генерации случайных чисел

def input_matrix(n: int):
    """Функция заполнения квадратной матрицы случайными числами
    Входные параметры:
    n - размер матрицы (n x n)
    Выходные параметры:
    a - матрица"""
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = random.randint(-CONST_D, CONST_D)
    return a

def output_matrix(n: int, a: list):
    """Процедура вывода матрицы
    Входные параметры:
    n - размер матрицы
    a - матрица"""
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()

def average_array(n: int, a: list):
    """Функция вычисления среднего арифметического элементов одномерного массива
    Входные параметры:
    n - размер массива
    a - одномерный массив
    Выходные параметры:
    avg - среднее арифметическое"""
    sum_elements = 0
    for i in range(n):
        sum_elements += a[i]
    avg = sum_elements / n if n != 0 else 0
    return avg

print("Программа вычисления среднего арифметического главной диагонали квадратной матрицы")
n = int(input('Введите размер квадратной матрицы: '))

matrix = input_matrix(n)
print('\nИсходная матрица:')
output_matrix(n, matrix)

main_diagonal = [matrix[i][i] for i in range(n)]

avg_main_diagonal = average_array(n, main_diagonal)
print(f'\nСреднее арифметическое элементов главной диагонали: {avg_main_diagonal:.2f}')