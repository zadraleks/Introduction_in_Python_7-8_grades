#Необходимо написать программу, выводящую кортеж, содержащий числа в полуинтервале [a; b), если a < b, и [b; a), если
# b < a. Числа a и b вводятся с клавиатуры.

a, b = int(input()), int(input())
if a < b:
    print(tuple(range(a, b)))
else:
    print(tuple(range(b, a)))
