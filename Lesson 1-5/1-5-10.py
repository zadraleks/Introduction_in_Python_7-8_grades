#Напишите программу, принимающую на вход год и выводящую "Високосный", если в этом году действительно 366 дней, и
#"Невисокосный" иначе. Год считается високосным, если его номер делится на 4, но не делится на 100 или же делится на
#400.

a = int(input())
if a % 4 == 0 and a % 100 != 0:
    print("Високосный")
elif a % 400 == 0:
    print("Високосный")
else:
    print("Невисокосный")