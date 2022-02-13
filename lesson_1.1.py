# 1.
number = input("Введите трехзначное число: ")

sum = 0
product = 1
for i in number:
    sum += int(i)
    product *= int(i)
print(f'Сумма цифр {number}: {sum}')
print(f'Произведение цифр: {number}: {product}')
