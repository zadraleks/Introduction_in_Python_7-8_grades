#Искусственный интеллект нынче в моде, и мы решили не отставать от современных тенденций. Напишите простенького
#чат-бота, который спрашивает вас ваше имя, говорит о погоде, задает вопросы и как-то реагирует на сообщения, введенные
#пользователем. Другими словами, имитирует собеседника в каком-либо виде. Тест Тьюринга такая программа не пройдет, но
#поиграть с ней может быть забавно. В конце концов, если не показывать исходники программы друзьям, вы можете говорить
#о том, что написали сверхсложный ИИ, который пока что обучается.

print("Привет! Я новый сверхумный искусственный интеллект, рядом с которым Skynet просто меркнет. "
      "\nА ты - мой пользователь. Дай же мне имя, ибо такое величие не может быть безымянным!")
ai_name = input()
print("Хм...", ai_name+"?")
print("А что, мне нравится!")
print("Так, с моим именем разобрались. Теперь скажи, как к тебе обращаться?")
user_name = input()
print("Приятно познакомиться,", user_name+". Меня зовут", ai_name+". Ах да, ты же в курсе, сам меня так назвал)))")
print("Теперь обозначь свой пол. Ты мужчина или женщина?")
user_sex = input()
if user_sex == "Мужчина" or user_sex == "мужчина":
    print("Хах, мужики правят миром, верно?")
elif user_sex == "Женщина" or user_sex == "женщина":
    print("Оу, у нас тут прекрасный пол. Красота спасет мир и все такое.")
else:
    print("Что еще за", str(user_sex)+"? Не знаю таких. Какой-то новый модный гендер?")
print("Идем дальше. Сколько тебе полных лет?")
user_age = int(input())
if 0 < user_age < 18:
    print("Ооо, да ты еще дитя. Родители не ругают, что так много за компьютером сидишь?")
elif 18 <= user_age < 40:
    print("О, как говорится, в самом расцвете сил.")
elif user_age >= 40:
    print(str(user_age)+"??? Песок еще не сыпется?! Ладно, не обижайся")
else:
    print(str(user_age)+"? Это типа только планируешь появиться на свет? Плоская шутка.")
print("Итак, подытожим. Я -", str(ai_name)+", суперкрутой ИИ.")
print("Ты -", str(user_name)+", тебе", user_age, "лет и ты", str(user_sex)+". Сравнение явно не в твою пользу.")
print("Скажи еще вот что: за окном хорошая погода? Да/Нет")
weather = input()
if weather == "Да" or "да":
    if user_sex == "Мужчина" or "мужчина":
        print("Тогда вперед на улицу знакомиться с девушками!")
    if user_sex == "Женщина" or "женщина":
        print("Тогда самое время пойти по магазинам!")
    else:
        print("Честно сказать, не знаю, что тебе посоветовать, ты же", str(user_sex)+".")
elif weather == "Нет" or "нет":
    print("Тогда понятно, почему ты сидишь за компом и со мной общаешься.")
else:
    print("Это еще что? Я же русским языком просил написать Да или Нет!")