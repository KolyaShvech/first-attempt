# letter_index = 0
# my_string = 'dsklggke'
# for letter in my_string:
#     print(letter + ' is at index ' + str(letter_index))
#     letter_index = letter_index + 1

# my_string = 'dsklggke'
# for item in enumerate(my_string):
#     print(item)
#
#
# my_string = 'dsklggke'
# for index, letter in enumerate(my_string):
#     print(letter + ' is at index ' + str(index))
#
#
#
# letter_list = ['a', 'b', 'c', True]
# print('a' in letter_list)
# print(True in letter_list)
#
# dict_1 = {1: 'a', 2: 'b', 3: 'c'}
# print(1 in dict_1)
# print(1 in dict_1.keys())
# print(4 in dict_1.keys())
#
# from random import shuffle
# my_list = [1, 34, 56, 32, 21]
# shuffle(my_list)
# print(my_list)
#
# from random import randint
# print(randint(1,10))
#
#
# x = int(input('Write number 1: '))
# y = int(input('Write number 2: '))
# if x > 0:
#     if y > 0:
#         print(x + y, x - y, x * y, x / y)
# elif x < 0:
#     if y < 0:
#         print(x + y, x - y, x * y, x / y)
# else:
#     print('Одного или оба значения равны 0')
# import math
# pi = 3.141592
# x = 1
# y = 2
# z = 3
# # print(round(pi, 3))
# # print(math.ceil(pi))
# # print(pow(pi, 2))
# # print(math.sqrt(pi))
# # print(max(x, y, z))
# # print(min(x, y, z))

# import random
# # numbers = random.random()
# # print(numbers)
# # numbers = random.random() * 100
# # print(numbers)
# # numbers = random.randint(10, 100)
# # print(numbers)
# # numbers = random.randrange(20)
# # print(numbers)
# # numbers = random.randrange(2, 20)
# # print(numbers)
# # numbers = random.randrange(2, 50, 2)
# # print(numbers)
#
# my_list = [1, 2, 3, 4, 5, 8, 9]
# random.shuffle(my_list)
# print(my_list)
# random_numbers = random.choice(my_list)
# print(random_numbers)
#
# import math
# d = 4.2
# print(math.sqrt(d))
# print(math.pow(d, 4))
# print(math.ceil(d))
# print(math.floor(d))
# print(math.factorial(5))
# print(math.degrees(d))
# print(math.radians(90))
# print(math.cos(math.radians(180)))
# print(math.sin(math.radians(180)))
# print(math.tan(math.radians(180)))
# print(math.log(9, 4))
# print(math.log10(200))
#
import locale
# locale.setlocale(locale.LC_ALL, 'de')
# # number = 12345.6789
# # converted = locale.format_string('%f', number)
# # print(converted)
# # converted = locale.format_string('%.2f', number)
# # print(converted)
# # converted = locale.format_string('%d', number)
# # print(converted)
# # converted = locale.format_string('%e', number)
# # print(converted)
# money = 872.679
# formatted = locale.currency(money)
# print(formatted)
#
# locale.setlocale(locale.LC_ALL, '')
# number = 7891.234
# formatted = locale.format_string('%.3f', number)
# print(formatted)
# print(locale.getlocale())

# def say_hallo(name):
#     print('Hello', name)
#
# say_hallo('Tommi')
# say_hallo('Will')
# say_hallo(123)

# def say_hallo(name='Tom'):
#     print('Hello', name)
#
# say_hallo()
# say_hallo('Sam')
#
# def display_info(name, age):
#     print('Name:', name, '\n', 'Age:', age)
# display_info(age=22, name='Pamela')
# display_info(age=45, name='Samanta')
#
# def sum(*params):
#     result = 0
#     for n in params:
#         result += n
#     return
#
# sum_of_numbers1 = sum(1, 2, 3, 4, 5, 6)
# sum_of_numbers2 = sum(5, 6, 7, 8, 9)
# print(sum_of_numbers1)
# print(sum_of_numbers2)

# def exchange(usd_rate, money):
#     result = round(money/usd_rate, 2)
#     return result
# result1 = exchange(27, 4500)
# print(result1)
# result2 = exchange(28, 21000)
# print(result2)
#
# def create_user():
#     name = 'Ron'
#     age = 32
#     return name, age
# user_name, user_age = create_user()
# print('Name:', user_name, '\t Age:', user_age)
#
# def main():
#     say_hello('Orest')
#     usd_rate = 28
#     money = 4000
#     result = exchange(usd_rate, money)
#     print('К выдаче', result, 'долларов')
#
# def say_hello(name):
#     print('Hi', name)
#
#
# def exchange(usd_rate, money):
#     result = round(money/usd_rate, 2)
#     return result
#
# main()

# def main():
#     say_hello("Tom")
#     usd_rate = 56
#     money = 30000
#     result = exchange(usd_rate, money)
#     print("К выдаче", result, "долларов")
#
#
# def say_hello(name):
#     print("Hello,", name)
#
#
# def exchange(usd_rate, money):
#     result = round(money / usd_rate, 2)
#     return result
#
#
# # Вызов функции main
# main()




