A = set(map(int, input("Введите множество A(через пробел): ").split()))
B = set(map(int, input("Введите множество B(через пробел): ").split()))
C = set(map(int, input("Введите множество C(через пробел): ").split()))
D = set(map(int, input("Введите множество D(через пробел): ").split()))

Z = ((B & C) - D) | ((A & B) - C)
print("Результат: {Z}")
