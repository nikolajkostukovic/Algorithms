#2
'''
В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.
'''
import random

list = random.sample(range(20),10)
print(f'Массив случайных чисел: {list}')

max = list[0]
min = list[0]

for i in list:
    if i > max:
        max = i

min_index = list.index(min)
max_index = list.index(max)
list[min_index], list[max_index] = list[max_index], list[min_index]
print(f'Массив после изменения элементов {min_index} и {max_index}: {list}')