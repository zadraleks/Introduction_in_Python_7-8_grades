#С клавиатуры вводится натуральное число, затем на другой строке число n <= длины числа. Выведите на экран последние n
#цифр числа.

a, n = int(input()), int(input())
print(a % (10**n))