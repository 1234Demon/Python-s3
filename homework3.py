# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import os
os.system("cls")

# n = int(input("Enter amount = "))
# for i in range(n):
#     list_math.append(input("Add smth in list: "))

list_math = [1.1, 1.2, 3.1, 5, 10.01]

max = list_math[0] - int(list_math[0])
min = list_math[0] - int(list_math[0])
i = 1

# b = list_math[0]
# a = b - int(b)
# print(a)

while i < len(list_math):
    if max < list_math[i] - int(list_math[i]):
        max = list_math[i] - int(list_math[i])
    if min > list_math[i] - int(list_math[i]):
        min = list_math[i] - int(list_math[i])
    i += 1

print(max - min)    