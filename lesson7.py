#1
'''
Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
'''

import statistics

def median_func(m):
    ls_item = len(m) -1
    for z in range(0,ls_item):
        for x in range(0,ls_item):
            if m[x] > m[x + 1]:
                m[x], m[x + 1] = m[x + 1], m[x]
    return m


items = [10, 90, 31, 96, 74, 56, 7, 11, 91, 73, 86, 62, 22]
print(f'Median = ',statistics.median(items))
print('Old List',items)
new = median_func(items).copy()
print('New List', new)
