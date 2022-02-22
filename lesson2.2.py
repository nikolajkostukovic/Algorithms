#2
''' Сформировать из введенного числа обратное по порядку
    входящих в него цифр и вывести на экран.
    Например, если введено число 3486,
    то надо вывести число 6843. (Сделать без использования строк)
'''

num = int(input('Введите число которое хотите перевернуть: '))
rever_num = 0

def recur_revers(num):
    global rever_num
    if (num > 0):
        Reminder = num %10
        rever_num = (rever_num *10) + Reminder
        recur_revers(num //10)
        return rever_num

rever_num = recur_revers(num)
print(f'Перевернутое число: = %d'% rever_num)

