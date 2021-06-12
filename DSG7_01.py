"""
Программа расчета сцепления для машин выпущенных до 05.2011 года
"""
# Общее

A0 = float(input("Введите расстояние до вала в см: "))
B1 = float(input("Введите расстояние до кольца слева в см: "))
B2 = float(input("Введите расстояние до кольца справа в см: "))

B = (((B1 + B2) / 2) - A0) * 10

print(f"Расстояние 'B' равно: {B:.2f} мм")

# К1

A1a = float(input("Введите расстояние для К1 до приблуды слева в см: "))
A1b = float(input("Введите расстояние для К1 до приблуды справа в см: "))
K1sc = float(input("Введите значение которое указано на сцепе со своим знаком для К1: "))

K1p = 52.4  # В мм  Постоянное значение приспособления для K1
K1g = 50.08  # В мм  Постоянное значение глубины установки для K1

A1 = (((A1a + A1b) / 2) - A0) * 10
K1 = A1 - B + K1p - K1g  # Расчетная толщина кольца

SK1 = K1 + K1sc  # Толщина кольца

print(f"Толщина кольца для К1 равна: {SK1:.2f} мм")
# print(f"толщина равна: {A1:.2f}-{B:.2f}+{K1p:.2f}-{K1g:.2f}+{K1sc:.2f}={SK1:.2f}")


# K2

A2a = float(input("Введите расстояние для К2 до приблуды слева в см: "))
A2b = float(input("Введите расстояние для К2 до приблуды справа в см: "))
K2sc = float(input("Введите значение которое указано на сцепе со своим знаком для К2: "))

K2p = 36.6  # В мм  Постоянное значение приспособления для K2
K2g = 34.35  # В мм  Постоянное значение глубины установки для K2

A2 = (((A2a + A2b) / 2) - A0) * 10
K2 = A2 - B + K2p - K2g  # Расчетная толщина кольца

SK2 = K2 + K2sc  # Толщина кольца

print(f"Толщина кольца для К2 равна: {SK2:.2f} мм")
