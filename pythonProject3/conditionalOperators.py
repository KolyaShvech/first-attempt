# x = 4
# if x > 3:
#     print('x > 3')
#     print('I\'m happy!')
# elif x < 3:
#     print('x < 3')
# else:
#     print('x == 3')


# day_time = 'midnight'
# if (day_time) == 'morning':
#     print('Monster wakes up')
# elif (day_time) == 'aftenoon':
#     print('Monster is walking')
# elif (day_time) == 'evening':
#     print('Monster is eating')
# elif (day_time) == 'night':
#     print('Monster is sleeping')
# else:
#     print('Monster is doing somethings')

# x = 45
# if x % 2 == 0:
#     print('x is even')
# else:
#     print('x is odd')

# user_input = input('Input something')
# if user_input == 'Hello':
#     print('Hello! Nice meet you.')
#
# lucky_number = input('Enter a number')
# if lucky_number:
#     print(lucky_number + ' is your lucky number')
# else:
#     print('You have enter some number, please try again')

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in number_list:
#     print(str(number) + ' Hola')
# for number in number_list:
#     if number % 2 == 0:
#         print(number)
#     else:
#         print('Hey')

# sum_number_list = 0
# for number in number_list:
#     sum_number_list = sum_number_list + number
# print(sum_number_list)

# tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# for item in tuple_list:
#     print(item)
# for letter1, letter2 in tuple_list:
#     print(letter1)
#     print(letter2)
#
# tuple_list1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
# for letter1, letter2, number in tuple_list1:
#     print(letter1, letter2, number)
#
#
# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# for item in dictionary:
#     print(item)
# for item in dictionary.items():
#     print(item)
# for item in dictionary.keys():
#     print(item)
# for item in dictionary.values():
#     print(item)
#
# for _ in range(5):
#     print('Hello')

# x = 5

# while x > 1:
#     print(x)
#     x = x - 1

# while x < 10:
#     print(x)
#     x += 1
#
# while x < 10:
#     print(x)
#     x += 2

x = 0
# while x < 10:
#     print (str(x) + (' x less than 10')
#     x += 1
# else:
#     print (str(x) + (' x now not less than 10')
#
#
# for x in range(10):
#     print(str(x) + ' x less than 10')
# else:
#     x += 1
#     print(str(x) + ' x now not less than 10')

# break, continue, pass

my_list = [1, 2, 3]

# for item in my_list:
#     if item ==2:
#         break
#     print(item)
# print('another code')

for item in my_list:
    if item ==2:
        continue
    print(item)
print('another code')