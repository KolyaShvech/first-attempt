# number_list = [32, 45, 87.23]
# print (number_list)
# some_list = [27, 89.987, "goo bye"]
# print(some_list)
# print(len(some_list))
# print(some_list[1])
# another_list = some_list[:2]
# print(another_list)
# some_list[2] = "hi"
# print(some_list)
#
# # Adding items
#
# new_list = some_list + another_list
# print(new_list)
# new_list.append("new item")
# new_list.insert(0, "start")
# new_list.insert(2, 13)
#
# # # Removing items
# # new_list.pop()
# # new_list.pop(0)
# # new_list.pop(-3)
#
# deleted_item =  new_list.pop()
# deleted_item = new_list.pop(-3)
# deleted_item = new_list.remove(13)
# print(new_list)
# print(deleted_item)

# number_list = [34, 43, 6, 76, 8]
# letter_list = ['s', 'e', 't', 'r']
# number_list.sort ()
# letter_list.sort()
# new_list = letter_list
#
# number_list.reverse()
# letter_list.reverse()
# new_list.append(letter_list)
# print (number_list)
# print (letter_list)

# m_l = [4, 5, 6, 7, 8, 9, 10]
# print(m_l[-1], m_l[0])     # Получение последнего и первого значения из списка
#
# a = 'Hi'
# b = 'Bye'
# print(a, b = b, a)
# print(a, b)

# this_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]   # Дан список
# for elem in this_list:    # Для элементов в списке
#     if elem < 8:          # Если элементы меньше 5
#         print(elem)      # То выводим эти елементы
#
# b = [1, 4, 6, 3, 5, 78, 65, 12, 89]
# for numbers in b:
#     if numbers < 45:
#         print(numbers)
# c = [78, 90, 67, 345, 93, 76, 82, 122, 56, 134]
# for values in c:
#     if values < 100:
#         print(values)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]   # первый список
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]   # Второй список
# result = [elem for elem in a if elem in b]  # Вывести элементы для элементов в списке А если елементы в списке В
# print(result)

# x = [1, 4, 6, 7, 9, 11, 14, 16, 17, 19, 23, 25, 27, 30]
# y = [1, 4, 7, 10, 12, 16, 19, 21, 22, 25, 30]
# z = [numbers for numbers in x if numbers in y]
# print(z)

# d = [3, 4, 6, 7, 9, 11, 15, 19, 21, 24, 28, 30, 32, 35]
# f = [2, 4, 6, 10, 12, 15, 16, 19, 22, 24, 29, 32, 36, 67]
# u = [elem for elem in d if elem in f]
# print(u)

#
# r = [2, 4, 5, 6, 7, 8, 9, 1, 0, 10, 12, 13, 14, 16, 17]
# e =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 20]
# w = [elem for elem in r if elem in e]
# print(w)


# r = [2, 4, 5, 6, 7, 8, 9, 1, 0, 10, 12, 13, 14, 16, 17, 11, 15]
# r.sort()
# print(r)
# r.sort(reverse=True)
# print(r)

# c = [78, 90, 67, 345, 93, 76, 82, 122, 56, 134]
# #c.sort()
# c.append('Allo')
# print(c)
# c.append([4, 5, 7])
# print(c)
# c.pop(3)
# print(c)

# c.sort(reverse=True)
# print(c)


# a = [0, 3, 4, 2, 1, 56, 43, 23, 76, 87, 90, 34, 23, 16, 12, 56, 72]
# a.sort()
# print(a)
# a.append('Good job!')
# print(a)
# a.pop(8)
# print(a)
# a.reverse()
# print(a)
# # a.extend(a)
# # print(a)
# a.pop()
# print(a)
# a.pop(4)
# print(a)
# a.count(5)
# print(a)
# a.insert(1, -1)
# print(a)
# a.insert(4, 3456)
# print(a)
# a[0] = 'Exelent'
# print(a)
# a[-1] = 'HOT'
# print(a)

# a = ['hi', 'Hi', 'HI', 'Hello', 'Hey', 'hey', 'good day', 'good morning']    # первая лист
# b = ['hi', 'Hi', 'ola', 'Hello', 'bye', 'hey', 'good evening', 'good morning']# второй лист
# c = [elem for elem in a if elem in b]   # вводим третий лист для опредения общих значений, значения для елем. в стр(А) если елем в строке (В)
# print(c)

#
# my_list = ['one', 'two', 'three', 'four', 'five']
# for elem in my_list:
#     print(elem)

# читаем елементы в строке
# b = ['hi', 'Hi', 'ola', 'Hello', 'bye', 'hey', 'good evening', 'good morning'] # строка с данными
# for elem in b:     # Для елементов в строке В
#     print(elem)    # ввыводим елементы
#
# a = ['hi', 'Hi', 'HI', 'Hello', 'Hey', 'hey', 'good day', 'good morning']
# for elem in a:
#     print(elem)
#
# a = [0, 3, 4, 2, 1, 56, 43, 23, 76, 87, 90, 34, 23, 16, 12, 56, 72]
# for k in range(len(a)):
#     a[k] += 2
# print(a)


# c = [78, 90, 67, 345, 93, 76, 82, 122, 56, 134]     # Дан список
# for i in range(len(c)):     # Для АЙ в диапозоне РАНЖ функция ЛЕН для возврата количества элементов списка С
#     c[i] -= 3     # список С с изменением АЙ "-= 3"
# print(c)       #Вывобим список С

# c = [78, 90, 67, 345, 93, 76, 82, 122, 56, 134, 90, 93, 90]
# # print(c[-1])
# # print(c[4])
# # print(c[6])
# c.insert(3, 122)
# print(c)
# print(c.index(93))
# c.remove(90)
# print(c)
# print(c[0:11:3])

# c = [78, 90, 67, 345, 93, 76, 82, 122, 56, 134, 90, 93, 90]
# print(len(c))
# print(max(c))
# print(min(c))
# print(sum(c))
# a = [0, 3, 4, 2, 1, 56, 43, 23, 76, 87, 90, 34, 23, 16, 12, 56, 72]
# # c = [78, 90, 67, 345, 93, 76, 82, 122, 56, 134, 90, 93, 90]
# # if a == c:
# #     print('Совпадат')
# # else:
# #     print('Не совпадают')
# # print(a + c)
# for k in range(len(a)):
#     a[k] += 2
# print(a)
#
# str = 'Batman and Joker'
# print(str.split())
# print(list(str))
#
# my_str = 'The sun shane is braitly'
# print(list(my_str))
# print(my_str.split())

# str = ['Joker', 'is', 'a', 'main', 'rival', 'of', 'batman!']
# delimetet = ' '
# output = delimetet.join(str)
# print(output)
#
# str = ['Today', 'I', 'go', 'with', 'my', 'freinds', 'to', 'sushi.']
# delimiter = ' '
# new_str = delimiter.join(str)
# print(new_str)

# str = ['Batman', 'and', 'Joker']
# str2 = str
# str2[2] = 'Robin'
# print(str)
# print(str2)
#
#
# my_str = ['Valet', 'Dama']
# my_str2 = my_str
# my_str2[1] = 'King'
# print(my_str)
#
# a = (23, 53, 'Victory', 'Elephant', {'lion': 12}, 2.12)
# b = [1, 3, 4, 6, 7, 6]
# c = list(a)
# d = tuple(b)
# print(c)
# print(d)

# countries = (
#     ('Germany', 80.2, (('Berlin', 3.326),('Hamburg', 1.718))),
#     ('France', 66, (('Paris', 2.2), ('Marsel', 1.6)))
# ) # Дан кортеж стран и городов
# for country in countries:   # Для стран в данном кортеже counrty
#     country_name, country_pollution, cities = country   # разделяем на переменные и прирявниваем их к кортежу country
#     print('\nCountry: {} population : {}'.format(country_name, country_pollution))   # Выводим с нижней строки страна, население
#     for city in cities:   # для городов в кортеже cities
#         city_name, city_populattion = city  # вводим переменные и приравниваем их к кортежу city
#         print('City : {} population : {}'.format(city_name, city_populattion))   #

# countries = (
#     ('Ukraine', 45.3, (('Kiev', 2.56),('Kharkov', 1.72))),
#     ('Poland', 34.6, (('Warshava', 2.12), ('Wroclav', 0.95))),
#     ('Spain', 56.8, (('Madrid', 6.34), ('Barcelona', 5.89))),
#     ('Holland', 32.78, ('Amsterdam', 3.42),('Rotterdam', 0.87)))
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nCountry: {} population: {}'.format(country_name, country_population))
#     for city in cities:
#         city_name, city_population = city
#         print('City: {} population: {}'.format(city_name, city_population))


# Действие со словарями
# dict = {'Iphone': 21000, 'Samsung': 19000, 'Xiomi': 8000}
# print(dict)
# my_list = [['Iphone', 21000], ['Samsung', 19000], ['Xiomi', 8000]]
# my_dict = dict(my_list)
# print(my_dict)
# lst = [
#     ['bred', 23],
#     ['eggs', 29],
#     ['milk', 26],
#     ['banana', 27]
# ]
# dct = dict(lst)
# print(dct)
# my_typle = (
#     ('bred', 23),
#     ('eggs', 29),
#     ('milk', 26),
#     ('banana', 27)
# )
# my_dct = dict(my_typle)
# print(my_dct)

# my_dict = {
#     'Iphone': 21000,
#     'Samsung': 19000,
#     'Xiomi': 8000
# }
# # print(my_dict['Iphone'])
# key = 'Samsung'   # обозначем переменную
# if key in my_dict:   # если переменная (key) в словаре
#     my_dict = my_dict[key]   # словарь приравниваем к значению ключа
#     print(my_dict)   # выводим значание
# else:   #  иначе
#     print('No this key!')   # выводим НЕТ ТАКОГО КЛЮЧА
#
#
# new_dict = {
#     'AI - 92': 27,
#     'AI - 92 premium': 29,
#     'AI - 95': 30,
#     'AI - 95 premuim': 33,
#     'AI - 98': 36
# }
# key = 'AI - 97'
# if key in new_dict:
#     new_dict = new_dict[key]
#     print(new_dict)
# else:
#     print('No this diesil!')
#
# prise = {
#     'headphones': 400,
#     'powerbank': 250,
#     'case': 320,
#     'charging': 150,
#     'litning': 230
# }
# key = input('Enter product that you need:')
# if key in prise:
#     prise = prise[key]
#     print(prise)
# else:
#     print('Have not this product')
#
products = {
    'bred': 23,
    'eggs': 29,
    'milk': 26,
    'banana': 27
}
# # del products['bred']
# # print(products)
# # del products['eggs']
# # print(products)
# key = 'oil'
# if key in products:
#     product = products[key]
#     del products[key]
#     print(product, 'deleted')
# else:
#     print('Have not this product')
# for key in products:
#     print(key, ' - ', products[key])
# for key, value in products.items():
#     print(key, ' - ', value)
# for key in products.keys():
#     print(key)
# for value in products.values():
#     print(value)
#
#
# n = range(1, 50)
# for numbers in n:
#     if numbers %2 != 0:
#         print(numbers)
#
# i = range(0, 50, 2)
# a = list(range(0, 50, 2))
# print(i)
# print(a)
# elem = int(input('Number: '))
# factorial = 1
# for n in range(1, elem + 1):
#     factorial *= n
# print('Factorial', elem, 'will be', factorial)
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end='\t')
#     print('\n')

# i = 0
# # while i < 10:
# #     print(i)
# #     i += 1
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1
#
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     if i == 5:
#         break
#     i += 1
#
# number = 23
# guess = int(input('Enter the number: '))
# if guess == number:
#     print('You luckyman! ')
# elif guess < number:
#     print('You not lucky ')
# else:
#     print('sorry not lucky')
# print('Stop program')
#
# number = 23
# running = True
# while running:
#     guess = int(input('Введите число: '))
#     if guess == number:
#         print('Вы угадали число!')
#         running = False
#     elif guess < number:
#         print('Вы не угадали число, но немного больше.')
#     else:
#         print('Вы не угодали число, оно немного меньше.')
# else:
#     print('Цикл while закончен.')
# print('Завершение')

# Lucky number
# num = 7
# run = True
# while run:
#     nums = int(input( 'Enter the number: '))
#     if nums == num:
#         print('You guessed the number!')
#         run = False
#     elif nums < num:
#         print(' You not guessed number it is bigger.')
#     else:
#         print('You not guessed number it is little more.')
# else:
#     print('While stoped')
# print('Stop program LUCKY NUMBER')
#
# while True:
#     s = input('Введите что-нибудь: ')
#     if s == 'выход':
#         break
#     if len(s) < 3:
#         print('Слишком мало букв ')
#         continue
#     print('Длина строки', len(s))
# print('Завершение')
#
# try:
#     number = int(input('Enter the number: '))
#     print('Entering number:', number)
# except ValueError as e:
#     print('conversion failed', e)
# finally:
#     print('Блок try завершил выпонение')
# print('Stop program')

# try:
#     number1 = int(input('Введите первое число:'))
#     number2 = int(input('Введите втророе число:'))
#     print('Деление двех чисел равна: ', number1/number2)
# except ValueError:
#     print('Преобразование прошло не удачно.')
# except ZeroDivisionError:
#     print('Попытка деления числа на ноль.')
# except Exception:
#     print('Общее исключение.')
# print('Работа завершена!')
#
# try:
#     number1 = int(input('Введите первое число:'))
#     number2 = int(input('Введите второе число:'))
#     if number2 == 0:
#         raise Exception('Второе число не должно быть равно 0')
#     print('Деление двух чисел равно:', number1/number2)
# except ValueError:
#     print('Введины некорректные данные!')
# except Exception as e:
#     print(e)
# print('Работа завершена!')


# class Person:
#     name = 'Tom'
#     def displace_info(self):
#         print('Меня зовут ', self.name)
# person1 = Person()
# person1.displace_info()
# person2 = Person()
# person2.name = 'Sammy'
# person2.displace_info()
# person3 = Person()
# person3.name = 'Monty'
# person3.displace_info()

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def display_info(self):
#         print('Меня зовет ', self.name)
# person1 = Person('Brandy')
# person1.display_info()
# person2 = Person('William')
# person2.display_info()

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def __del__(self):
#         print(self.name, 'Удалоно имя')
#     def display_info(self):
#         print('Мое имя ', self.name)
# person1 = Person('London')
# person1.display_info()
# del person1
# person2 = Person('Paris')
# person2.display_info()



