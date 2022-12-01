# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input("Введите число: "))

def fibona(n):
    a, b = 0, 1
    ls = []
    for _ in range(n + 1):
        ls.append(a)
        a, b = b, a + b
    return ls

def fibona_second(fib):
    ls = []
    for i in range(len(fib) - 1, 0, -1):
        if i % 2 == 0:
            ls.append(fib[i] * -1)
        else:
            ls.append(fib[i])
    return ls

f = fibona(n)
s = fibona_second(f)
print(s + f)
