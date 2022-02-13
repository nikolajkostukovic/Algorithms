#грокаем алгоритмы
def year(n):
    input_year = int(input('Введите год: '))
    if input_year %400 == 0:
        print('Этот год високосный!')
        return
    elif input_year %100 == 0:
        print('No вискосный год..((')
    elif input_year % 4 == 0:
        print('Этот високосный!')

    else:
        print('Не висоскосный!')
        year(n -1)

year(1)