# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

import os
os.system("cls")

a = int(input('Enter numb = '))
b = ''

while a > 0:
    b = str(a % 2) + b
    a = a // 2
 
print(b)