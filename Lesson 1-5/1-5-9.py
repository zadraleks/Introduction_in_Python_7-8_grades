#Улучшим нашу программу из задачи "Две операции арифметики", чтобы программа могла принять на вход также знак умножения
#("*") и деления ("/").

a, b = float(input()), float(input())
c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
else:
    print(a / b)