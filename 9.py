# Программа lab9_1
# Пример по теме одномерные массивы
# Программист: Морозов А. П., гр. 444
# Проверил: Бурмистров А. С.
# Дата написания: 12.02.25
# Переменные:
#   maslen - длина массива
#   arr - массив


maslen = int(input("Введите длину массива: "))
arr = []
lsum = 0
kount=0
for i in range(0, maslen):
    arr.append(float(input("Введите значения в массив: ")))

# Эхо вывод массива
print("Массив: ")
for el in arr:
    print(el, end=' ')
print()
for el in arr:
    lsum = el + lsum
    kount += 1
byr = lsum/kount
print(f"среднее значение среди всех положительных элементов: {byr}")
