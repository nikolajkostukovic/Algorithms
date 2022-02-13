class Chars:
    def random_chars(self):
        self.letter = the_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        index = int(input('Введите номер буквы: '))
        print(the_letters[index-1])

a = Chars()
a.random_chars()