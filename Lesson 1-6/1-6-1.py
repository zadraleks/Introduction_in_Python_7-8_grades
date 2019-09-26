#Список худших паролей почти не меняется из года в год, однако люди часто не придают большого значения безопасности в
#интернете. Один из ваших предыдущих клиентов хочет запустить валидацию пароля на своем сайте и попросил вас написать
#для него простенькую программу. Программа принимает на вход строку с паролем и выводит “Bad password”, если
#выполняется хотя бы одно из условий:
#пароль содержит подстроку qwerty или подстроку 1234
#пароль короче восьми символов
#пароль не содержит ни одну цифру
#и "Good password" иначе.

password = input()
if ("qwerty" in password or "1234" in password) or (len(password) < 8) \
        or ("1" not in password and "2" not in password and "3" not in password and "4" not in password
            and "5" not in password and "6" not in password and "7" not in password and "8" not in password
            and "9" not in password and "0" not in password):
    print("Bad password")
else:
    print("Good password")