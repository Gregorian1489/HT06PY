# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно 
# ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.

list_1 = []
a1 = int(input('Введите первый элемент списка: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов списка: '))

for i in range(n):
    list_1.append(a1 + i*d)
print(list_1)    
