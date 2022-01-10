# name = ''
#
# while len(name) == 0:
#     name = input('Enter you name: ')
#
# print('Hello ' + name)

#
# name = None
#
# while not name:
#     name = input('Enter you name: ')
#
# print('Hello ' + name)

# import time         Программа обратного отчета
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print('Happy new Year')

# rows = int(input('How many rows you need?: '))   Вложенный цикл
# columns = int(input('How many columns you need?: '))
# symbol = input('Enter the symbol to use: ')
# for i in range(rows):
#     for r in range(columns):
#         print(symbol, end='')
#     print()
#  BREAK, CONTINUE, PASS
# while True:
#     name = input('enter your name: ')
#     if name != '':
#         break

# phone_numbers = '123-456-1234'
#
# for numbers in phone_numbers:
#     if numbers == '-':
#         continue
#     print(numbers, end='')

# for i in range(1, 15):
#     if i == 13:
#         pass
#     else:
#         print(i)

# drink = ['coffee', 'soda', 'tea']
# dinner = ['hamburger', 'pizza', 'hotdog']
# desert = ['cake', 'ice cream']
#
# foods = [drink, dinner, desert]
# print(foods[0][0])


# def multiply(number1, number2):
#     return number1 * number2
# x = multiply(6, 8)
# print(x)

#
# def hello(first, middle, last):
#     print('Hello' + first + ' ' + middle + ' ' + last)
# hello(last='Cagual', middle='Senivaly', first='Endy')

# num = input('Enter a whole positive number: ')
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
#
# print(round(abs(float(input('Enter a whole positive number: ')))))
#


# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
# print(add(1, 2, 3, 4, 5, 6, 7 ))

# def hello(**kwargs):
#     print('Hello', end=' ')
#     for key, value in kwargs.items():
#         print(value, end=' ')
#
#
#
# hello(title='Mr.', first='Nick', middle='Valeriv', last='Shvechykov')

#
# animal = 'cow'
# item = 'moon'
# #print('The ' + animal + ' jumped over the ' + item )
# print('The {} jumped over the {}'.format(animal, item))
#
# name = 'Nick'
# print('Hello, my name is {}'.format(name))
# print('Hello, my name is {:10}. Nice meet you'.format(name))
# print('Hello, my name is {:>10}. Nice meet you'.format(name))
# print('Hello, my name is {:<10}. Nice meet you'.format(name))
# print('Hello, my name is {:^10}. Nice meet you'.format(name))


# number = 1000
# print('The number pi {:.3f}'.format(number))
# print('The number pi {:,}'.format(number))
# print('The number pi {:b}'.format(number))
# print('The number pi {:o}'.format(number))
# print('The number pi {:x}'.format(number))
# print('The number pi {:e}'.format(number))

# import random   Random
#
# x = random.randint(1, 6)
# y = random.random()
#
# my_list = ['Rock', 'coffee', 'scissors']
# z = random.choice(my_list)
#
# cards = [1, 2, 3, 4, 5, 6, 7, 'd', 'a', 't']
# random.shuffle(cards)
# print(x)
# print(y)
# print(z)
# print(cards)

# Exception Исключение
#
# try:
#
#     numerator = int(input('Enter a number to divide: '))
#     dominator = int(input('Enter a number to divide by: '))
#     result = numerator/dominator
# except ZeroDivisionError as e:
#     print(e)
#     print('You can not divide by zero')
# except ValueError as e:
#     print(e)
#     print('Enter only numbers please!')
# except Exception as e:
#     print(e)
#     print('Something went wrong!')
# else:
#     print(result)
# finally:
#     print('This will always execute!')

# File detection \ Обнаружение файла
# import os
#
# path = 'C:\\Foto and video\\Urban fest 2020'
#
# if os.path.exists(path):
#     print('That location exists. ')
#     if os.path.isfile(path):
#         print('This is file.')
#     elif os.path.isdir(path):
#         print('This is a directory.')
# else:
#     print('That location does not exists.')

#  Read file\ Чтение файла
# try:
#
#     with open('C:\\Foto and video\\test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File was not find!')

# Write a file\ Написание файла
# text = 'Yooohhha!\nI write in another file.\nThis is asome!\nHow i can find you?'
# with open('C:\Foto and video\\test.txt', 'w') as file:
#     file.write(text)

# Copy file\Копирование файла
#
# import shutil
# shutil.copyfile('C:\\Foto and video\\test.txt', 'C:\\Foto and video\\test_copy.txt')

# Move a file\ Перемещение файла

# import os
# source = 'testing.txt'
# destination = 'C:\\Foto and video\\testing.txt'
#
# try:
#     if os.path.exists(destination):
#         print('There is file already here.')
#     else:
#         os.replace(source,destination)
#         print(source + ' was moved.')
# except FileNotFoundError:
#     print(source + ' was not found.')


# Game ROCK PAPER SCISSOR \ ИГРА КАМЕНЬ НОЖНИЦЫ БУМАГА

# import random
# while True:
#
#     choices = ['rock', 'paper', 'scissors']
#
#     computer = random.choice(choices)
#     player = None
#
#     while player not in choices:
#         player = input('rock, paper or scissors?: ').lower()
#     if player == computer:
#         print('Player: ', player)
#         print('Computer: ', computer)
#         print('Tie!')
#     elif player == 'rock':
#         if computer == 'paper':
#             print('Player: ', player)
#             print('Computer: ', computer)
#             print('You lose!')
#         if computer == 'scissors':
#             print('Player: ', player)
#             print('Computer: ', computer)
#             print('You win!')
#     elif player == 'paper':
#         if computer == 'scissors':
#             print('Player: ', player)
#             print('Computer: ', computer)
#             print('You lose!')
#         if computer == 'rock':
#             print('Player: ', player)
#             print('Computer: ', computer)
#             print('You win!')
#     elif player == 'scissors':
#         if computer == 'rock':
#             print('Player: ', player)
#             print('Computer: ', computer)
#             print('You lose!')
#         if computer == 'paper':
#             print('Player: ', player)
#             print('Computer: ', computer)
#             print('You win!')
#
#     play_again = input('Play again?(y/n): ').lower()
#     if play_again != 'y':
#         break
# print('Bye!')
#
# from car import Car
#
# car_1 = Car('Chevy', 'Corvette', 2021, 'green')
# car_2 = Car('Ford', 'Mustang', 2020, 'black')
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.colors)
#
# car_1.drive()
# car_1.stop()

# Inheritance \ Наследие классы
# class Animals:
#     alive = True
#
#     def eat(self):
#         print('This animal is eating.')
#     def slumber(self):
#         print('This animal is sleeping.')
#
# class Rabbit(Animals):
#     def run(self):
#         print('This animal is run.')
#
# class Fish(Animals):
#     def swim(self):
#         print('This animal is swimming')
#
# class Hawk(Animals):
#     def fly(self):
#         print('This animal is flying.')
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# # print(rabbit.alive)
# # fish.eat()
# # hawk.sleep()
# rabbit.run()
# fish.swim()
# hawk.fly()

# multi-level inheritance\ многоуровневое наследие

# class Organism:
#
#     alive = True
#
# class Animals(Organism):
#
#     def eat(self):
#         print('This animal is eating.')
#
# class Dog(Animals):
#     def bark(self):
#         print('This animal is barking.')
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()


# MULTIPLY INHERITANCE \ МНОЖНСТВЕННОЕ НАСЛЕДИЕ

# class Prey:
#
#     def flee(self):
#         print('This animal is flees.')
#
# class Predator:
#
#     def hunt(self):
#         print('This animal is hunting')
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit()
# hawk =Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# METHOD CHAINIG \ ЦЕОЧКА МЕТОДОВ

# class Car:
#
#     def turn_on(self):
#         print('You start the engine.')
#         return self
#
#     def drive(self):
#         print('You drive the car.')
#         return self
#
#     def brake(self):
#         print('You stop on the brakes.')
#         return self
#
#     def turn_off(self):
#         print('This turn off is the engine.')
#         return self
#
#
# car = Car()
# #car.brake().turn_on()
# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

# SUPER FUNCTION\ СУПЕР ФУНЦИЯ
#
# class Restangle:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#
# class Square(Restangle):
#
#     def __init__(self, lenght, width):
#         super().__init__(lenght, width)
#
#     def area(self):
#         return self.lenght * self.width
#
#
# class Cube(Restangle):
#
#     def __init__(self, lenght, width, height):
#         super().__init__(lenght, width)
#         self.height = height
#
#     def volume(self):
#         return self.lenght * self.width * self.height
#
#
# square = Square(3, 4)
# cube = Cube(3, 6, 5)
#
# print(square.area())
# print(cube.volume())


# ABSTRACT CLASSES \ АБСТРАКТНЫЕ КЛАССЫ

# from abc import ABC, abstractmethod
#
# class Vehicle:
#
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def go(self):
#         print('You goes in car.')
#
#     def stop(self):
#         print('This car is stopped.')
#
# class Motorcycle(Vehicle):
#     def go(self):
#         print('You goes in the bike.')
#
#     def stop(self):
#         print('This motorcycle is stopped.')
#
#
# #vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# #vehicle.go()
# car.go()
# motorcycle.go()
#
# car.stop()
# motorcycle.stop()

# OBJECT AS ARGUMENT\ ОБЪЕКТ КАК АРГУМЕНТ   изменение цвета транспорта

# class Car:
#
#     color = None
#
# class Motorcycle:
#
#     color = None
#
# def change_color(vehicle, color):
#
#     vehicle.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
# bike_1 = Motorcycle()
#
# change_color(car_1, 'Red')
# change_color(car_2, 'Green')
# change_color(car_3, 'Purple')
# change_color(bike_1, 'white')
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)

# class Duck:
#
#     def walk(self):
#         print('Duck is walking.')
#
#     def talk(self):
#         print('Duck is qwuacing.')
#
# class Chicken:
#
#     def walk(self):
#         print('Chicken is walking.')
#
#     def talk(self):
#         print('Chicken is clucking.')
#
#
# class Person:
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print('You caught the critter')
#
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)

# -------------WALRUS OPERATOR\ МОРЖОВЫЙ ОПЕРАТОР

# foods = list()
# while True:
#     food = input('What food do you like? ')
#     if food == 'quit':
#         break
#     foods.append(food)

# foods = list()
# while food := input('What food do you like? ') != 'quit':
#     foods.append(food)

# cars = list()
# while car := input('What car do you want? ') != 'quit':
#     cars.append(car)

# -------------HIGHER ORDER FUNTION \ ФУНКИЯ ВЫСШЕГО ПОРЯДКА

# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()
# def hello(func):
#     text = func('Hello')
#     print(text)
#
# hello(quiet)
# hello(loud)

# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend
# divide = divisor(2)
# print(divide(10))

# def difference(x):
#     def term(y):
#         return y - x
#     return term
#
# subtrahend = difference(5)
#
# print(subtrahend(16))

# def sum(x):
#     def item(y):
#         return y + x
#     return item
#
# subtrahend = sum(78)
# print(subtrahend(127))


# ------------------LAMBDA FUNCTION\ ЛЯМБДА ФУНКИЯ

# def double(x):
#     return x * 2
# print(double(5))

# #double = lambda x: x * 2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x + y + z
# full_name = lambda first_name, last_name: first_name +' ' + last_name
# age_check = lambda age: True if age >= 18 else False
# print(age_check(24))
# print(full_name('Kolya', 'Shvech'))
# print(add(7, 3, 8))

# ---------------SORT LIST, FUCTION\ СОРТИРОВКА ДЛЯ ЛИСТОВ И ФУНКЦИЯ

# studets = ('Lena', 'Vitya', 'Kolya', 'Sveta', 'Natasha', 'Ruben')
#
# #studets.sort(reverse=True)       # ДЛЯ СПИСКА
# sorted_studets = sorted(studets, reverse=True)     # ДЛЯ КОРТЕЖА
#
# for i in sorted_studets:
#     print(i)
#
# studets = (('Kolya', 'B', 32),
#            ('Sveta', 'A', 35),
#            ('Ira', 'C', 30),
#            ('Natasha', "F", 29),
#            ('Filip', "D", 31)
#            )
# age = lambda ages: ages[2]
# #studets.sort(key=grade)
# #studets.sort(key=age)
# sorted_studets = sorted(studets, key= age, reverse=True)
# for i in sorted_studets:
#     print(i)

# MAP FUCTION\ ФУНКЦИЯ КАРТЫ

# store =[
#     ('shirt', 20.00),
#     ('pants', 30.00),
#     ('jackets', 45.00),
#     ('socks', 10.00)
# ]
#
# to_euro = lambda data: (data[0], data[1] * 0.82)
# to_dollars = lambda data: (data[0], data[1]/0.82)
# store_dollars = list(map(to_dollars, store))
#
# for i in store_dollars:
#     print(i)


# --------------FILTER FUNCTION \ ФИЛЬТЕР

# friends = [
#     ('Ros', 21),
#     ('Rachel', 23),
#     ('Chendler', 20),
#     ('Fibi', 25),
#     ('Monika', 19),
#     ('Joi', 22)
# ]
#
# age = lambda data: data[1] >= 21
#
# older_friends = list(filter(age, friends))
#
# for i in older_friends:
#     print(i)

# REDUCE FUNCTION\ ФУНКЦИЯ УМЕНЬШЕНИЯ

#import functools
# letter = ['H', 'E', 'L', 'L', 'O']
#
# word = functools.reduce(lambda x, y: x + y, letter)
# print(word)
#
# factorial = [6, 5, 4, 3, 2, 1]
#
# result = functools.reduce(lambda x, y: x * y, factorial)
# print(result)


# -----------------lIST COMPREHESTIONS\ СПИСОК ПОНИМАНИЯ


# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)
#
# squares = [i * i for i in range(1, 11)]
# print(squares)

# studets = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
#
# # passes_students = list(filter(lambda x: x >= 60, studets))
# # passed_students = [i for i in studets if i >= 60]
# passed_students = [i if i >= 60 else 'FAILED' for i in studets]
#
# print(passed_students)

# -------------DICTIONARY COMPREHATION \ ПОНИМАНИЕ СЛОВАРЯ

# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angels': 100, 'Chicago': 50}
#
# cities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}
#
# print(cities_in_C)

# weather = {'New York': 'snowing', 'Boston': 'sunny', "Los Angels": 'sunny', 'Chicago': 'cloudy'}
#
# sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
# print(sunny_weather)

# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angels': 100, 'Chicago': 50}

# temperature = {key: ('warm' if value >= 40 else 'cold') for (key, value) in cities_in_F.items()}
# print(temperature)

# def check_temp(value):
#     if value >= 70:
#         return "HOT"
#     elif 69 >= value >= 40:
#         return "WARM"
#     else:
#         return 'COLD'
#
#
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angels': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key, value) in cities_in_F.items()}
#
# print(desc_cities)


# -------------------ZIP FUNCTIONS \ ЗИП ФУНКЦИЯ

# user_names = ['Nikolay', 'Shvechikov', 'Mister']
# password = ('p@sswords', 'gorshok123', 'guist')
# login_date = ['27/12/2021', '23/12/2021', '28/12/2021']
#
# users = zip(user_names, password, login_date)
# for i in users:
#     print(i)

# users = dict(zip(user_names, password))
# print(type(users))
# for key, value in users.items():
#     print(key + ' : ' + value)


# --------------------TIME MODULE\ МОДУЛЬ ВРЕМЯ


import time

# print(time.ctime(0))
#
# print(time.ctime(time.time()))
#
# time_object = time.localtime()
# print(time_object)
#
# local_time = time.strftime('%B, %D, %Y, %H:%M:%S', time_object)
# print(local_time)
#
# time_tuple = (2021, 12, 29, 12, 59, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

