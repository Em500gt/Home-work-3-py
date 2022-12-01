# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint, random

def random_list(count):
    li = [randint(0, 10) * round(random(), 2) for _ in range(int(count))]
    return li

def fractional_part(ls):
    s = [round(ls[i] % 1, 2) for i in range(len(ls))]
    max = s[0]
    min = s[0]
    for i in range(1, len(s)):
        min = s[i] if min > s[i] else min
        max = s[i] if max < s[i] else max
    
    return max - min

lst = random_list(input("Введите длину массива: "))

print(f"{lst} -> {fractional_part(lst)}")