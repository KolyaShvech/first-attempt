# exchange
# usd = 26
# euro = 31
#
# money = int(input('What sum you exchange: '))
# currency = int(input('write code currency (dollars - 400), (euro - 401): '))
# if currency == 400:
#     cash = round(money/ usd, 2)
#     print('Валюта доллары Сша')
# elif currency == 401:
#     cash = round(money/ euro, 2)
#     print('Валера евро')
# else:
#     cash = 0
#     print('неизвестная валета')
# print('К получению', cash)

# факториал
# number = int(input('Введите число '))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print('Факториал числа', number, 'равен', factorial)
#
# for i in range(1, 9):
#     for j in range(1, 9):
#         print(i * j, end= '\t')
#     print('\n')



# print('Для выхода нажмите Y')
#
# while True:
#     data = input('Введите сумму для обмена ')
#     if data.lower() == 'y':
#         break
#     money = int(data)
#     cache = round(money / 56, 2)
#     print('К выдаче', cache, 'долларов')
# print('Работа обменного пункта завершена')
#
#
# x = [1, 3, 5, 7, 9, 12, 15, 18, 21]
# y = [1, 2, 4, 5, 6, 9, 12, 14, 17, 21, 23]
# print([elem for elem in x if elem < 15])
# print([elem for elem in x if elem <20])
# result = list(filter(lambda elem: elem in x, y))
# print(result)
# result = [elem for elem in x if elem in y]
# result = list(set(x)& set(y))
# print(result)
#
#
# import operator
# d = {2: 4, 3: 2,5: 6, 7: 1, 6: 0 }
# result = dict(sorted(d.items(), key=operator.itemgetter(1)))
# print(result)
# result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# print(result)
#
#
# dict_a = {'Misha': 21, 'Lena': 19}
# dict_b = {'Sasha': 27, 'Yula': 29}
# dict_c = {'Vitya': 25, 'Sveta': 22}
# result = {}
# for d in (dict_a, dict_b,dict_c):
#     result.update(d)
# print(result)
#
# my_dict = {'do': 390, 're': 100, 'mi': 670, 'fa': 786, 'sol': 1280, 'lya': 420}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:5]
# print(result)

#
# def pascal_triangle(n):
#     row = [2]
#     y = [0]
#     for x in range(max(n, 0)):
#         print(row)
#         row = [left + right for left, right in zip(row + y, y + row)]
#
# pascal_triangle(8)
#
#
# def pascal_trangle(n):
#     row = [3]
#     y = [0]
#     for x in range(max(n, 0)):
#         print(row)
#         row = [left + right for left, right in zip(row + y, y + row)]
#
# pascal_trangle(10)
#
# my_string = [
#     'Лёша на полке клопа нашёл',
#     'лёша на полке клопа нашёл',
#     'нашел клопа на полке Лёша']
#
# def check_in_palindrome(string) :
#     preperad_str = string.replace(' ', '').lower
#     if preperad_str == preperad_str[::-1]:
#         return True
#     else:
#         return False
# if '__name__' =='__main__':
#     for items in my_string:
#         print('Строка является палидромом: ', check_in_palindrome(items))
#
#
# print('Stop process, press Y')
#
# while True:
#     data = input('Enter a number: ')
#     if data.lower() == 'y':
#         break
#     money = int(data)
#     if money < 0:
#         print('The number must be positive!')
#         continue
#     money = int(data)
#     cash = round(money / 0.4, 2)
#     print('Your sum', cash, 'rubley')
# print('Process completed')

