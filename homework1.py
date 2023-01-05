# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import os
os.system("cls")

# n = int(input("Enter amount = "))
# for i in range(n):
#     list_math.append(input("Add smth in list: "))

list_math = [2, 3, 5, 9, 3]
sum = 0
i = 1

while i < len(list_math) - 1:
    sum = sum + list_math[i]
    i += 2

print(sum)