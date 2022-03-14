



# a = int(input("Введите левое значение"))
# b = int(input("Введите среднее значение"))
# c = int(input("Введите правое значение"))
# i = int(input("Введите значение i"))
# j = int(input("Введите значение j"))

a = 2
b = 6
c = 5
i = 7
j = 3

numbers_list = [a, b, c]
numbers_list1 = [0, i, 0]
numbers_list2 = [0, -j, 0]
print(f'Изначальный массив: {numbers_list}')
numbers_list.sort()
print(f'Отсортированный массив: {numbers_list}')

res_lt1 = [numbers_list[x] + numbers_list1[x] for x in range(len(numbers_list1))]
res_lt2 = [numbers_list[x] + numbers_list2[x] for x in range(len(numbers_list2))]

print(f'Новый массив, где второй элемент массива ({numbers_list[1]}) + i ({numbers_list1[1]}) : {str(res_lt1)}')
print(f'Новый массив, где второй элемент массива ({numbers_list[1]}) - j ({numbers_list2[1]}) : {str(res_lt2)}')


if numbers_list[a<b]:
    print('YES')
else:
    print('NO')

if numbers_list[a<c]:
    print('YES')
else:
    print('NO')

if numbers_list[b<c]:
    print('YES')
else:
    print('NO')


# print(a)
# print(b)
# print(c)

#
# sort1 = a, b, c
# sort2 = a, b + d, c
# sort3 = a, b - f, c
# print(sort1)
# print(sorted(sort1))
# print(sorted(sort2))
# print(sorted(sort3))

#
#     if a<=c and d<=b:
#         print(f'значение {c} ,больше {a} и меньше {b}. Произведена сумма {f}+{c} ')
#         print(f'значение {d} ,больше {a} и меньше {b}. Произведена сумма {f}-{d} ')
#
#     return sorted([a, b, f])[1]
#
# kuk(a , b , c, d, f)
# print()
