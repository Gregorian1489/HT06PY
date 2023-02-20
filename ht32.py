#  Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

num = int(input('Введите длину списка: '))
list = list()
min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))

for i in range(num):
        list.append(random.randint(0,10))
print(list)        

for i in range(num):
        if min <= list[i] <= max:
            print(i)


