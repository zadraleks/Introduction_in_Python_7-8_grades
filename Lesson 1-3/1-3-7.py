#Возможно, вам интересно, сколько секунд содержится в одном году или, например, в жизни человека (взяв среднюю продолжительность жизни в 70 лет). С помощью языка Python теперь вы можете это выяснить!
#Формат ввода: целое число — количество лет. Считайте, что в году 365 дней, т. е. год не високосный.
#Формат вывода: целое число — количество секунд.

a = int(input())
print(a * 365 * 24 * 60 * 60)