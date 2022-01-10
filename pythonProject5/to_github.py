
# -----------------Вывести нечетные\ (четные) значения из списка, остановаться когда встретится значение 145
# def even(num1):
#         return num1 % 2 == 0 # --------нечетные
#         #return num1 % 2 != 0
# list1 = [2, 3, 5, 7, 12, 23, 43, 55, 66, 54, 125, 76, 89, 145, 102, 456, 76, 82]
# for item in list1:
#         if item == 145:
#                 break
#         if not even(item):
#                 print(item)


# -------------из листа вывести значения которые меньше 30 и кратные 3. Вычеслить сумму всех значений
# list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20, 12, 27, 45, 24, 56, 33]
# sm = 0
# for item in list:
#         if (item < 30) and (item % 3 == 0):
#                 print(item)
#         else:
#                 sm += item
# print('Sum ', sm)

# -------------------- Треуголник Паскаля
def pascal_triangle(n):
    row = [2]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


pascal_triangle(8)


# ----------------------Обмен валют
# usd = 27
# euro = 30
# rub = 0.4
# funt = 36
#
# money = int(input('Enter your number: '))
# currency = int(input('Укажите код валюты:\nдолары - (400),\nевро - (401),\nрубли - (402),\nфунты - (403): '))
# if currency == 400:
#     cash = round(money/usd, 3)
#     print('Валета доллары: ', cash)
# elif currency == 401:
#     cash = round(money/euro, 3)
#     print('Валета евро: ', cash)
# elif currency == 402:
#     cash = round(money/rub, 3)
#     print('Валера рубли: ', cash)
# elif currency == 403:
#     cash = round(money/funt, 3)
#     print('Валета фунты: ', cash)
# else:
#     print('Валета не известна!')
# print('К получению: ', cash)


# ------------------Факториал числа
# number = int(input('Введите число: '))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print('Факториал для', number, 'равен', factorial)
#
# for i in range(0, 10):
#     print(i)

# -------------------Таблица умножения
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end='\t')
#     print('\n')