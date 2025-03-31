# lab 11_3
# Кортежы
# Дата написания: 12.03.2025
# Програмист: Морозов А. П.
# Проверил: Бурмистров А. С. 
# Переменные:
    #input_tuple - ввод кортежа
    #element_to_remove - ввод элемента
    # index_to_remove - индекс первого элемента
    #result_tuple - результат

# Ввод кортежа
input_tuple = tuple(map(int, input("Введите кортеж чисел через пробел: ").split()))

# Ввод элемента, который нужно удалить
element_to_remove = int(input("Введите элемент для удаления: "))

# Поиск индекса первого вхождения элемента
index_to_remove = -1
for i in range(len(input_tuple)):
    if input_tuple[i] == element_to_remove:
        index_to_remove = i
        break

# Формирование нового кортежа
if index_to_remove != -1:
    # Если элемент найден, удаляем его
    result_tuple = input_tuple[:index_to_remove] + input_tuple[index_to_remove + 1:]
else:
    # Если элемент не найден, оставляем кортеж без изменений
    result_tuple = input_tuple

# Вывод результата
print("Результат:", result_tuple)