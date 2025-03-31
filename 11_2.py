# lab 11_2
# Кортежы
# Дата написания: 12.03.2025
# Програмист: Морозов А. П.
# Проверил: Бурмистров А. С. 
# Переменные:
    #input_tuple - ввод кортежа
    #element - ввод элемента
    #first_index, second_index - индексы первого и второго вхождения в элемент
    #result_tuple - результат

# Ввод кортежа
input_tuple = tuple(map(int, input("Введите кортеж чисел через пробел: ").split()))

# Ввод элемента
element = int(input("Введите элемент: "))

# Поиск индексов первого и второго вхождения элемента
first_index = -1
second_index = -1

# Поиск первого вхождения
for i in range(len(input_tuple)):
    if input_tuple[i] == element:
        first_index = i
        break

# Поиск второго вхождения (если первое найдено)
if first_index != -1:
    for i in range(first_index + 1, len(input_tuple)):
        if input_tuple[i] == element:
            second_index = i
            break

# Формирование результата
if first_index == -1:
    # Если элемент не найден
    result_tuple = tuple()
elif second_index == -1:
    # Если элемент встречается только один раз
    result_tuple = input_tuple[first_index:]
else:
    # Если элемент встречается дважды или более
    result_tuple = input_tuple[first_index:second_index + 1]

# Вывод результата
print("Результат:", result_tuple)