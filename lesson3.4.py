#4
'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
так и различаться.
'''


import random

list = random.sample(range(20),10)
print(f'Массив случайных чисел: {list}')

min_index_1 = 0
min_index_2 = 1

sort_list = []
sort_list.extend(list)
sort_list.sort()

print(f'Два наименьших элемента (второй способ): {sort_list[0]} и {sort_list[1]}')