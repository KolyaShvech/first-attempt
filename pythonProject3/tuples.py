# tuple_1 = (1, 2, 3)
# tuple_2 = ('one', 'hello', 'apple')
# tuple_3 = (2, 3.4, 'three')
# print(tuple_1[1])
#
# new_tuple = (tuple_1[0], 3, tuple_1[2])
# print(new_tuple)
# print(type(tuple_1))
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)

x = y = z = 12
x, y, z = 12, 13, 14
print(x, y, z)

person_tuple = ('Jonh', 'Smith', 1986)
first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)

t_1 = (1, 2, 5, 1, 10)
print(t_1.count(1))
greeting_tuple = ('hello', 'hi', 'hey', 'hi')
print(greeting_tuple.count('hi'))
print(t_1.index(1))
print(greeting_tuple.index('hi'))
