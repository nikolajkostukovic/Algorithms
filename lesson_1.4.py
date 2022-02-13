import random

class Random:
    def number_randit(self):
        self.s = start = 1
        self.sp = stop = 15
        integer = random.randint(start,stop)
        print(f'Случайное целое число: ',integer)

    def number_unif(self):
        self.s = start = 1
        self.sp = stop = 15
        integer = random.uniform(start, stop)
        print(f'Случайное вещественное число: ', integer)

    def random_choise(self):
        self.list =  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print(f'Случайный символ: ',random.choice(chars))

a = Random()
a.number_randit()
a.number_unif()
a.random_choise()

