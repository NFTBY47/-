arr = []
spislen = int(input())

for i in range(0, spislen):
    arr.append(float(input("введите значение которое хотите добавить в список: ")))
print()
print("Ваш список: ")
for el in arr:
    print(el)

unicARR = []
for value in arr:
    if value not in unicARR:
        unicARR.append(value)
unic_count = len(unicARR)
print(f"Количество уникальных значений в заданном вами списке: {unic_count}")