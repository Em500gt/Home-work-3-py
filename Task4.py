# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

numb = int(input("Введите число: "))
s = ''
while numb != 0:
    s = str(numb % 2) + s
    numb //= 2

print(int(s))