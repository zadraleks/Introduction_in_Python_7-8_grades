#Прямоугольная (или декартова) система координат широко применяется в математике. Напишите программу, которая принимает
#два целых, неравных нулю числа — координату точки по оси OX и по оси OY, и выведите, в какой координатной четверти
#находится точка.

x, y = int(input()), int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)