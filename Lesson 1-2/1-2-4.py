#С вами связался работник ФСБ, который хочет получить информацию о пользователях рунета. Он попросил вас написать
#программу, которая поочередно спрашивает пользователя его имя и фамилию, адрес, любимый цвет, паспортные данные и
#т. д., запоминает ответ, а в конце выводит всю информацию о пользователе в формате:
#Факт 1: значение 1
#Факт 2: значение 2
#и т. д.
#Данная задача проверяется преподавателем, так что вы можете проявить свою фантазию в полной мере.

print('Ваше имя:')
name = input()
print('Ваша фамилия:')
surname = input()
print('Ваш адрес:')
adress = input()
print('Ваш любимый цвет:')
color = input()
print('Серия и номер паспорта:')
passport = input()

print('\nДосье потенциального террориста:')
print('Имя:', name)
print('Фамилия:', surname)
print('Адрес:', adress)
print('Любимый цвет:', color)
print('Паспорт:', passport)
print('\nФСБ. За вами уже выехали.')