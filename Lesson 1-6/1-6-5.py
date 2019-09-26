#Программисты тоже любят играть в шахматы (в основном, на компьютере), и нередко за них это делают программы. Напишите
#программу, которая принимает на вход четыре числа: сначала координаты начального положения короля на шахматной доске,
#затем координаты клетки, куда игрок хочет походить. Вам необходимо вывести "YES", если игрок может походить королем из
#клетки в клетку за один ход, и "NO" иначе. Гарантируется, что изначально король находится на доске. Нумерация рядов и
#столбцов доски начинается с 1.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 == x2 and y1 == y2) or x2 < 1 or x2 > 8 or y2 < 1 or y2 > 8:
    print("NO")
elif abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
    print("YES")
else:
    print("NO")