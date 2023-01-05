# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

import os
os.system("cls")

n = int(input('Enter numb = '))
list_origin = [5, 3, 7, 4, 6]
list_change = [5, 3, 7, 4, 6]
cont = 0
i = 0

while i < len(list_origin):
    if i + n < len(list_origin):
        list_change[i + n] = list_origin[i]
        
    if i + n >= len(list_origin):
        list_change[i + n - len(list_origin)] = list_origin[i]
    
    i += 1

print(list_change)
