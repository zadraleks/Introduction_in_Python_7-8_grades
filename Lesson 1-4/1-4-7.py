#Представьте, что вы работаете на заводе (с программистами такое тоже случается) по производству пирожков. Вас
#попросили написать программу, которая принимает на вход цену одного пирожка в рублях и копейках, а затем количество
#пирожков — целое число. Вывести нужно итоговую стоимость пирожков в рублях и копейках через пробел.

a, b, c = int(input()), int(input()), int(input())
kops = (a * 100) + b
print((c * kops) // 100, (c * kops) % 100)
