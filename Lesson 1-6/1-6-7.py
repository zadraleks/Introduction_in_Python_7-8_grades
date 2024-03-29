#Одна из лучших РПГ-игр всех времен известна своими многочисленными версиями для самых разных платформ. Например,
#совсем недавно была анонсирована очередная версия игры: https://www.youtube.com/watch?v=FnEW6dX_BmU
#Однако похоже, что еще никто не создал версии на языке Python. У вас есть возможность исправить данное упущение и
#создать свою текстовую версию этой игры!
#Текстовый квест не обязан быть связан со Skyrim или с какой-либо другой игрой. Это может быть авторский продукт без
#ограничений на время прохождения (тем не менее программа не должна быть слишком короткой), вариативность сюжета и
#количество квестов/персонажей.
#Вы можете объединяться в группы по два-три человека.
#Данная задача проверяется преподавателем.
#Критерии оценивания:
#1) ﻿Текстовый квест содержит сюжет или подобие его. ﻿Максимум ﻿3 балла.
#2) ﻿Квест содержит несколько персонажей. Количество баллов за этот пункт зависит от количества персонажей, играющих
# более-менее важную роль в повествовании. Максимум 4 балла.
#3) Баллы за этот пункт выставляются за качество описания локаций и персонажей. Максимум ﻿3 балла.

print("Наступил вечер. Вы возвращаетесь домой после работы. Подходя к своему подъезду, вы замечаете, что возле "
      "входа расположилась большая компания людей явно гоповатого вида. Спортивные штаны, туфли, семки, орущий блатняк"
      "из старенького телефона. Гопники расположились основательно и не собираются никуда уходить. Но, похоже, вас они"
      "еще не заметили. Что будете делать? Выберите действие и введите его цифру.")
print("1. Развернуться и быстро уйти со двора.")
print("2. Сделать лицо кирпичом и зайти в подъезд.")
action_1 = int(input())
if action_1 == 1:
    print("Вы резко меняете траекторию движения и успеваете скрыться из поля зрения компании, пока там идет активное "
          "обсуждение семечек разных марок. Однако домой попасть как-то надо. Погрузившись в раздумия, вы остановились "
          "на двух вариантах. Выберите действие и введите его цифру.")
    print("1. Залезть на свой балкон со стороны улицы (благо, всего второй этаж).")
    print("2. Подождать, пока кто-то из других жильцов будет возвращаться домой и зайти вместе с ним.")
    penetration = int(input())
    if penetration == 1:
        print("Вы не придумали ничего лучше, чем залезть на свой балкон. Собравшись с духом, вы начинаете лезть по "
              "балкону первого этажа. Увы, жильцы этой квартиры не в восторге от вашей затеи и приняли вас за "
              "домушника. К несчастью, у них есть ружье и они не постеснялись пустить его в дело. Лёжа на земле под"
              "балконом в луже собственной крови, последние секунды своей жизни вы тратите на размышления о том, что "
              "где-то в жизни вы свернули не туда...")
        print("Конец игры")
    if penetration == 2:
        print("Рассудив, что если пройти в подъезд вдвоем, то эта компания не посмеет вас тронуть, вы решаете подождать "
              "кого-то из жильцов. И вскоре смутнознакомый мужчина (из 33-й квартиры, что ли?) направляется к двери "
              "подъезда. Вы ненавязчиво присоединяетесь к нему.")
#Дальше писать лень