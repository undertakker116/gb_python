# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
num = int(input("Введите день неделт для проверки на выходной: "))
weekends = [6, 7]
if num in weekends:
    print('Да, выходной')
elif num > 7:
    print('число больше семи')
else:
    print("Нет, рабочий день")

# 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(x, y, z)


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
try:
    x = int(input('Введите X: '))
    y = int(input('Введите Y: '))
    if x == 0 or y == 0:
        print("X or Y не должны ровнятся 0")
    if x > 0 and y > 0:
        print('1 quarter')
    elif x < 0 and y > 0:
        print('2 quarter')
    elif x < 0 and y < 0:
        print('3 quarter')
    elif x > 0 and y < 0:
        print('4 quarter')

except ValueError:
    print("Вы вывели не число")

# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)


quarter = int(input("Введите номер плоскости: "))
try:
    if quarter == 1:
        print("x > 0 and y > 0")
    elif quarter == 2:
        print("x < 0 and y > 0")
    elif quarter == 3:
        print("x < 0 and y < 0")
    elif quarter == 4:
        print('x > 0 and y < 0')
    else:
        print("Число вне диапозона")
except ValueError:
    print("Вы ввели строку")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print("Координаты точки А")
x_1, y_1 = int(input()), int(input())
print("Координаты точки Б")
x_2, y_2 = int(input()), int(input())

print(f'{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:0.4}')
