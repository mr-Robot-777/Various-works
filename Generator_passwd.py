import random

# Вариант 1

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "[]{}()*;:/,_-%№@$!#=+^&<>"

passwd = lower + upper + numbers + symbol
length = int(input("\nВведите длину пароля (до 87 символов): "))
password = "".join(random.sample(passwd, length))
print("--------------------------------------------------")
print("Ваш пароль: ")
print(password)
print("--------------------------------------------------")


# Вариант 2 более короткий но менее красивый чем первый

passwd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]{}()*;:/,_-%№@$!#=+^&<>"
length = int(input("\nВведите длину пароля (до 87 символов): "))
password = "".join(random.sample(passwd, length))
print("--------------------------------------------------")
print("Ваш пароль: ")
print(password)
print("--------------------------------------------------")
