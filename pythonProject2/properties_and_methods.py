# # Immutable
# first_name = "Jake"
# print (first_name [2])
#
# first_two_letters = first_name [:2]
# print (first_two_letters)
# last_letter = first_name [-1:]
# print (last_letter)
#
# # Concantenable
# new_first_name = first_two_letters + "n" + last_letter
# print (new_first_name)
#
# greeting = "Hello"
# greeting = greeting + " Python!"
# print (greeting)
#
# # Myltiplication
# ymmy = "yum "
# print (ymmy * 3)
#
# print(ymmy.upper())
# print(ymmy.lower())
#
# long_string = "This is long string"
# print (long_string.split("s"))
# print (long_string.split())

# car_price = {"opel" : 5000, "toyota" : 7000, "bmv" : 10000}
# print(car_price)
# print (car_price['toyota'])
# car_price['mazda'] = 4000
# print(car_price)
# del car_price['toyota']
# print(car_price)


person = {
    'first name' : 'Jack',
    'last name' : 'Brown',
    'age'  : 43,
    'hobbies' : ['football', 'singing', 'photo'],
    'children' : {'son' : 'Michael', 'dauther' : 'Pamela'}

}
print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])
print(person['hobbies'][2])
children = person['children']
print(person['children']['son'])
person ['car'] = 'mazda'
person ['hobbies'][0] = 'basketball'
print(person.keys())
print(person.values())
print(person.items())