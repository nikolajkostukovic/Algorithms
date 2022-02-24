#3
'''
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

import random

list = random.sample(range(20),10)
print(f'Массив случайных чисел: {list}')

max_index = 0
min_index = 0
step = 1
sum = 0

for i in list:
    if list[min_index] > i:
        min_index = list.index(i)
    elif list[max_index] < i:
        max_index = list.index(i)

if max_index - min_index < 0:
    step = -1

for i in list[min_index + step:max_index:step]:
    sum += i

print(f'Сумма элементов между минимальным ({list[min_index]})\n, и максимальным ({list[max_index]}) элементами: {sum}')