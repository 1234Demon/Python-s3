# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

import os
os.system("cls")

n = int(input('Enter numb = '))
list_fibon = [1, 0, 1]
i1 = 2
i2 = 2
sum_up = 1
sum_dwn = -1

while i1 <= n:
    list_fibon.append(sum_up)
    sum_up = list_fibon[i1] + list_fibon[i1 + 1]
    i1 += 1


while i2 <= n:
    list_fibon.insert(0, sum_dwn)
    sum_dwn = -(list_fibon[0] - list_fibon[1])
    i2 += 1

print(list_fibon)