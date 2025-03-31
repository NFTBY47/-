# lab 12
# Кортежы
# Дата написания: 17.03.2025
# Програмист: Морозов А. П.
# Проверил: Бурмистров А. С. 
# Переменные:
    # all_students
    #sport_students
    #art_students
    #sport_or_art_students
    #not_sport_not_art_students
# Условие задачи: 

# Вводим кол-во и имена всех студентов
all_students = int(input("Введите общее кол-во студентов: "))
all_students_set = set()
for i in range(0, all_students):
    all_students_set.add(str(input("Введите имена всех студентов: ")))

# Вводим кол-во и имена студентов занимающихся спортом
students_sport = int(input("Введите кол-во студентов занимающихся спортом: "))
students_sport_set = set()
for j in range(0, students_sport):
    students_sport_set.add(str(input("Введите имена студентов зан. спортом")))

#Вводим имена и кол-во студентов занимающихся искусством
students_art = int(input("введите кол-во студентов занимающихся искусством"))
students_art_set = set()
for k in range(0, students_art):
    students_art_set.add(str(input("Введите имена студентов зан. искусством")))
#Находим студентов спорт или искусство
sport_or_art_students = all_students_set.union(students_art_set)
#Находим студентов ни спорт не искусство
not_sport_not_art_students = all_students_set - sport_or_art_students
print(f"Студенты не занимающиеся ни спортом не искусством: {not_sport_not_art_students}")