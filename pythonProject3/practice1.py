# number = [1, 2, 3, 4, 5, 6 ,7]
# number.append(str('Kolya'))
# number [4] = 176
# number.append(['Hi', 'car', 'yes', 'apple'])
# number [-3] = (1, 67, 12)
# number.remove(176)
# print(number)
# print (number[0])
# print (number[-1])
# print(number.count(4))

#
# user_list = [
#     ['+111111', 'Tom'],
#     ['+222222', 'Jack'],
#     ['+234555', 'Alice']
# ]
# user_dict = dict(user_list)
# print(user_dict)
#
#
# user_tuple = (
#     ('+111111', 'Tom'),
#     ('+222222', 'Jack'),
#     ('+234555', 'Alice')
# )
# user_dict = dict(user_tuple)
# print(user_dict)

#
# my_dict = {
#         'Bob': 34,
#         'Nick': 28,
#         'Tom': 51
# }
# del my_dict ['Tom']
# print(my_dict)
# # key = 'Jony'
# # if key in my_dict:
# #     user = my_dict[key]
# #     print(user)
# # else:
# #     print('No elements')
# # key = 'Bob'
# # my_dict = my_dict.get(key)
# key = 'Tom'
# if key in my_dict:
#     my_dict1 = my_dict[key]
#     del my_dict [key]
#     print(my_dict1, 'delete')
# else:
#     print('No elements')
#
#
# users = {
#         'Bob': 34,
#         'Nick': 28,
#         'Tom': 51
# }
# key = 'Nick'
# user = users.pop(key)
# print(user)
#
# user = users.pop('Leam', 'Unknown users')
# print(user)
#
#
# users = {
#         'Bob': 34,
#         'Nick': 28,
#         'Tom': 51
# }
# users2 = users.copy()
# print (users, users2)
#
# users = {
#         'Bob': 34,
#         'Nick': 28,
#         'Tom': 51
# }
# users2 = {
#         'Ella': 45,
#         'Tim': 12,
#         'Yohan': 43
# }
# users.update(users2)
# print(users)
# print(users2)
# #
# for key in users:
#         print(key, ' - ', users[key])
# for key, value in users.items():
#         print(key, ' - ', value)
# for key in users.keys():
#         print(key)
# for value in users.values():
#         print(value)
#
# person = {
#         'Jim': {
#                 'phone': '+380956547895',
#                 'email': 'jim.hokins@gmail.com'
#         },
#
#         'Andy':{
#                 'phone': '+380661234573',
#                 'email': '+380972563214',
#                 'skype': 'AndyPanda'
#         }
# }
# for key in person:
#         print(key, ' - ', person['Andy'])
#         print(key, ' - ', person['Jim'])
#
#
# list = ['zero', 1, 2, 3, 4, (5, 5, 5)]
# print(list[0])
# print(list[-1])
# a = 100
# b = 'litera'
# a, b = b, a
# print(a)
# print(b)
#
# z = 20
# s = 10
# z, s = s, z
# print(z)
# print(s)
#
#
# age1 = 45
# age2 = 23
# age1, age2 = age2, age1
# print(age1)
# print(age2)
#
# list = [0, 1, 0, 3, 0, 1, 4 ,5]
# st = set(list)
# print(st)
#
# my_dict = {'eggs': 30, 'milk': 28, 'meat': 120}
# my_dict['oil'] = 90
# my_dict[('it', 'is', 'tuple')] = [11, 22, 'list_value', 33, {1, 2, 3}]
# for key in my_dict:
#         print(key)
# keys = my_dict.keys()
# print(my_dict.keys())
#
# st = {'it', 'is','set',1 }
# print(st)
# frozen_st = ({'it', 'is','frozen','set',2 })
# union = st | frozen_st
# print(frozen_st)
# print(union)
# intersection = st & frozen_st
# print(intersection)
#
# def even(num):
#         return num % 2 == 0
# list = [1, 23, 34, 54, 87, 99, 102, 123, 134, 139, 546, 675, 876]
# for item in list:
#         if item == 139:
#                 break
#         if not even(item):
#                 print(item)
#
#
#
#
# def even(num1):
#         return num1 % 2 == 0
# list1 = [2, 3, 5, 7, 12, 23, 43, 55, 66, 54, 125, 76, 89, 102, 456, 76, 82, 145]
# for item in list1:
#         if item == 145:
#                 break
#         if not even(item):
#                 print(item)
#
# list = []
# for item in range(18, 1, -4):
#         list.append(item)
# print(list)
#
# list = []
# for item in range(21, 1, -2):
#         list.append(item)
# print(list)
#
#
#   Действие со списком
#
# median = 30
# div_num = 3
# list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# sm = 0
# for item in list:
#         if (item < median) and (item % div_num == 0):
#                 print(item)
#         else:
#                 sm += item
# print('Sum ', sm)
#
# list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20, 12, 27, 45]
# sm = 0
# for item in list:
#         if (item < 30) and (item % 3 == 0):
#                 print(item)
#         else:
#                 sm += item
# print('Sum ', sm)
#
#
# Вывидение ключа из кортежа
#
# def month_to_season(month):
#         season_ranges = {
#                 (12, 1, 2) : 'Winter',
#                 (3, 4, 5) : 'Spring',
#                 (6, 7, 8) : 'Summer',
#                 (9, 10, 11) : 'Autumn'
#         }
#         season = None
#         for key, value in season_ranges.items():
#                 if month in key:
#                         season = value
#                         break
#         return season
# print(month_to_season(12))
# print(month_to_season(2))
# print(month_to_season(5))
# print(month_to_season(19))
# print(month_to_season(10))
#   Действие со строками (первое упражнение)
#
#
# my_list = 'Сидел барсук в своей норе и ел картошечку пюре'
# print(my_list)
# print(len(my_list))
# print(my_list + str('.'))
# print('ре' in my_list)
# print(my_list.count('ре'))
# print(my_list[-2])
# print(my_list[1::2])
# print(my_list.count(' '))
#
#    Действие со строками
# my_str = 'ели мясо мужики, пивом запивали '
# print(my_str)
# print(len(my_str))
# print(my_str + str('!'))
# print('ли' in my_str)
# print(my_str.count('ли'))
# print(my_str[-3])
# print(my_str[1::2])
# print(my_str.count(' '))
#
# string = 'пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.'
# print(string.capitalize())
# print(string.find('сопровождать'))
# print(string.index('сопровождать'))
# print(string.replace('сопровождать', 'не сопровождать').capitalize())
# print(string.split(','))
# print(''.join(string))
#
#        Сумма числа всех цифр
# NUM = 12345
# def sum_for(num) :
#         s = 0
#         for item in str(num):
#                 s = s + int(item)
#         return s
# print(sum_for(NUM))
#
# Num = 13579
# def sum_list(num):
#         lst = [int(item) for item in str(num)]
#         return sum(lst)
# print(sum_list(Num))
#
#
#   Измение заданной постройки
# STR = '01101011101011'
# print(STR.replace('1', '0', 1))
# print(STR.replace('1', '0', 5))
# print(STR.replace('1', '0'))
# print(STR.replace('1', '0', 9))
# print(STR.replace('1', '0', 10))


#  Является ли строка палидромом
# TEST = [
#         'Лёша на полке клопа нашёл',
#         'лёша на полке клопа нашёл',
#         'нашел клопа на полке Лёша']
# def checn_if_palindrome(string):
#         preperad_str = string.replace(' ', '').lower()
#         if preperad_str == preperad_str[::-1]:
#                 return True
#         else:
#                 return False
# if __name__ == '__main__':
#         for item in TEST:
#                 print('Строка является палидромом: ', checn_if_palindrome(item))

#  Меняем слова местами в строке
# def swap_words(string):
#         lst = string.split(' ')
#         lst.reverse()
#         return ' '.join(lst)
# if __name__ == '__main__':
#         print(swap_words('идет снег'))
#         print(swap_words('снег идет давно'))



# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for item in a:
#         if item < 5:
#                 print(item)
# print([elem for elem in a if elem < 5])
# result = list(filter(lambda elem: elem in a, b))
# print(result)
# result = [elem for elem in a if elem in b]
# result = list(set(a)& set(b))
# print(result)

#  сортировка словаря по возростанию и убыванию
#
# import operator
# d = {1: 2, 3: 4,4: 3, 2: 1, 0: 0 }
# result = dict(sorted(d.items(), key=operator.itemgetter(1)))
# print(result)
# result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# print(result)
#
#
# dct_1 = {1: 10, 4: 40}
# dct_2 = {2: 20, 5: 50}
# dct_3 = {3: 30, 6: 60}
# result = {}
# for d in (dct_1, dct_2, dct_3):
#     result.update(d)
# print(result)
#
#
# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(result)

#
# def pascal_triangle(n):
#     row = [1]
#     y = [0]
#     for x in range(max(n, 0)):
#         print(row)
#         row = [left + right for left, right in zip(row + y, y + row)]
#
#
# pascal_triangle(6)


# def pascal_triangle(n):
#     row = [1]
#     y = [0]
#     for x in range(max(n, 0)):
#         print(row)
#         row = [left + right for left, right in zip(row + y, y + row)]
#
#
# pascal_triangle(6)

#
# def is_palidrome(string):
#     return string == ''.join(reversed(string))
# print(is_palidrome('abba'))
#
#
# def is_palidrome(string):
#     return string == string[::-1]
# print(is_palidrome('abba'))
# #
# def is_palindrome(string):
#     return string == ''.join(reversed(string))
#
# print(is_palindrome('abba'))
# #
#
# def convert(seconds):
#     days = seconds // (24*3600)
#     seconds %= 24*3600
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f'{days}:{hours}:{minutes}:{seconds}')
# convert(1234565)
#
#
# a = '24'
# b = 67
# c = int(a) + b
# print(c)
# c = int(a) - b
# print(c)
# c = int(a) * b
# print(c)
# c = int(a) / b
# print (round(c,4))
# c = int(a) ** b
# print(c)
# c = int(a) % b
# print(c)
# c = int(a) // b
# print(c)
#
#
# y = 8
# x = 9
# print(y < x)
# print(y > x)
# print(y <= x)
# print(y >= x)
# print(y != x)
# print(y == x)

#
# age = 32
# name = 'Nick'
# weight = 70.7
# not_married = True
# full_info = age <= 32 and name and weight == 70.7 and not_married
# print(full_info)
#
# age = 31
# weight = 80
# married = True
# full_info = age > 30 and weight == 80 and married == True
# print(full_info)
#
# month = 16
# done = True
# result = month > 17 or done == False
# print(result)
#
# print('Tomorrow will \tbe better\nthen yesterady')
#
# str = 'winter'
# str1 = 'summer'
# print(str.title())
# print(str1.title())
#
#
# age = 50
# if age < 50:
#     print('Your welcome')
# elif age == 50:
#     print('Ok, hello')
# else:
#     print('Good bay')
# print('Suscess')
#
# age = 79
# if age < 18:
#     print('less years then 18')
# elif age >= 18:
#         print('more then 18')
# elif age > 21:
#         print('more then 21')
# else:
#         print('from 18 until 21')

# Обмен валют
# usd = 27
# euro = 30
# rub = 0.4
# funt = 36
#
# money = int(input('Enter your number: '))
# currency = int(input('Укажите код валюты:\nдолары - (400),\nевро - (401),\nрубли - (402),\nфунты - (403): ' ))
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
# #
# choice = 'y'
# while choice.lower() == 'y':
#     print('Hello')
#     choice = input('Для продолжения нажмите Y, а для выхода любую другую клавишу: ')
# print('Работа заверщина ')

# Факториал числа
# number = int(input('Введите число: '))
# i = 1
# factorial = 1
# while i <= number:
#     factorial *= i
#     i += 1
# print('Факториал', number, 'равен', factorial)

# Факториал числа
# number = int(input('Введите число: '))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print('Факториал для', number, 'равен', factorial)
#
# for i in range(5):
#     print(i, end=' ')

# Таблица умножения
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end='\t')
#     print('\n')
#
# print('Для выхода нажмите Y')
#
# while True:
#     data = input('Введите сумму: ')
#     if data.lower() == 'y':
#         break
#     money = int(data)
#     cash = round(money / 27, 2)
#     print('К выдаче ', cash, 'долларов')
# print('Процесс завершен!')
#
#
# print('If you want stoped, press Y ')
#
#
# while True:
#     data = input('Enter a number: ')
#     if data.lower() == 'y':
#         break
#     money = int(data)
#     if money < 0:
#         print('the number must be positive!')
#         continue
#     money = int(data)
#     cash = round(money / 30, 2)
#     print('Your sum', cash, 'euro')
# print('Process completed ')
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j,end='\t')
#     print('\n')

#
#
#
# number = int(input('Введите число: '))
#
# factorial = 1
# for i in range(1, number +1):
#     factorial *= i
# print('Для значения', number, 'равен', factorial)

#
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')
    print('\n')
#
#
# car = 45
# doll = 95
# ball = 100
# candy = 78
#
# product = int(input('Введите количество: '))
# kod = int(input('Код продукта:\ncar - (100)\ndoll - (200)\nball - (300)\ncandy - (400):'))
# if kod == 100:
#     numbers = product * car
#     print('Сумма равна ', numbers)
# elif kod == 200:
#     numbers = product * doll
#     print('Сумма равна ', numbers)
# elif kod == 300:
#     numbers = product * ball
#     print('Сумма равна ', numbers)
# elif kod == 400:
#     numbers = product * candy
#     print('Сумма равна ', numbers)
# print('Приготовить сумму равную ', numbers)



# сумма n + nn + nnn
# def solve(n):
#     n1 = n
#     n2 = int(str(n) * 2)
#     n3 = int(str(n) * 3)
#     print(n1 + n2 + n3)
# solve(2)
#

# Вывести четные числа в заданном списке и остановиться, когда встретит 237
# my_num = [2, 4, 10, 23, 34, 54, 65, 80, 100, 134, 167, 189, 201, 207, 208, 214, 223, 234, 237, 256, 287, 301, 306]
# for n in my_num:
#     if n == 237:
#         break
#     elif n % 2 == 0:
#         print(n)





