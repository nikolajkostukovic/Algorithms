n1, n2, n3 = [x for x in input('Введите три числа, через пробел: ').split()]

if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Среднее: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Среднее: {n2}')
else:
    print(f'Среднее: {n3}')