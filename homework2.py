# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import os
os.system("cls")


# n = int(input("Enter amount = "))
# for i in range(n):
#     list_math.append(input("Add smth in list: "))

list_math = [2, 3, 4, 5, 6]
list_sum = list()
i = 0

while i <= len(list_math) - 1 - i:
    list_sum.append(list_math[i] * list_math[len(list_math) - i - 1])
    i += 1

print(list_sum)