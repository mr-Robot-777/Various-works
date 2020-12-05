import random

# Вариант 1

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbol = "[]{}()*;:/,_-%№@$!#=+^&<>"

login = upper + lower + numbers
passwd = upper + lower + numbers + symbol

length_log = int(input("\nВведите длину Логина (до   62  символов): "))
length_pass = int(input("Введите длину Пароля (до  87   символов): "))

login =  "".join(random.sample(login, length_log))
password = "".join(random.sample(passwd, length_pass))
print("--------------------------------------------------")
print("Ваш  логин: ", login)
print("Ваш пароль: ", password)
print("--------------------------------------------------")


# Вариант 2 более короткий но менее красивый чем первый
#
# passwd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]{}()*;:/,_-%№@$!#=+^&<>"
# length = int(input("\nВведите длину пароля (до 87 символов): "))
# password = "".join(random.sample(passwd, length))
# print("--------------------------------------------------")
# print("Ваш пароль: ")
# print(password)
# print("--------------------------------------------------")
