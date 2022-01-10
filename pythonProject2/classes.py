# class Person:
#     def __init__(self, name):
#         self.name = name
#     def dislay_info(self):
#         print('Мое имя ', self.name)
#
# class Auto:
#     def __init__(self, name):
#         self.name = name
#      def move(self, speed):
#          print(self.name, 'едет со скоростью', speed, 'км/ч')
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
#     def display_info(self):
#         print('Имя', self.name, '\tВозраст', self.age)
# tom = Person('Tom')
# tom.name = 'Человек-паук'
# tom.age = -129
# tom.display_info()

# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1
#     def set_age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print('Вы ввели неправильное значение')
#     def get_age(self):
#         return self.__age
#     def get_name(self):
#         return self.__name
#     def display_info(self):
#         print('Имя', self.__name, '\tВозраст', self.__age)
# tom = Person('Tom')
#
# tom.display_info()
# tom.set_age(0)
# tom.set_age(21)
# tom.display_info()
#
# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = int(input('Возраст'))
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print('Недоступный возраст')
#     @property
#     def name(self):
#         return self.__name
#     def display_info(self):
#         print('Имя', self.__name, '\tВозраст', self.__age)
# tom = Person('Tom')
#
# tom.display_info()
# tom.age = 34
# print(tom.age)
# tom.age = 37
# tom.display_info()
#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print('Возраст не подходит.')
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print('Имя', self.__name, '\tВозраст', self.__age)
#
# class Emplyee(Person):
#     def details(self, company):
#         print(self.name, 'работает в компании', company)
#
# tom = Emplyee('Tom', 25)
# tom.details('Bolt')
# tom.age = 33
# tom.display_info()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#             print('Возраст не дуступен')
#     def display_info(self):
#         print('Имя', self.__name, '\tВозраст', self.__age)
# class Empolyee(Person):
#     def __init__(self, name, age, company):
#         Person.__init__(self, name, age)
#         self.company = company
#
#     def display_info(self):
#         Person.display_info(self)
#         print('Компанмя', self.company)
#
# class Student(Person):
#     def __init__(self, name, age, university):
#         Person.__init__(self, name, age)
#         self.university = university
#     def display_info(self):
#         print('Студент', self.name, 'Учится в университете', self.university)
#
# people = [Person('Tom', 23), Student('Bob', 19, 'Harvard', ), Empolyee('Sam', 35, 'Uber')]
#
# for person in people:
#     person.display_info()
#     print()
#
# for person in people:
#     if isinstance(person, Student):
#         print(person.university)
#     elif isinstance(person, Empolyee):
#         print(person.company)
#     else:
#         print(person.name)
#         print()


#
#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#             print('Возраст не дуступен')
#     def display_info(self):
#         print('Имя', self.__name, '\tВозраст', self.__age)
#
# tom = Person('Tom', 23)
# print(tom)

#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print('Возраст не дуступен')
#     def display_info(self):
#         print(self.__str__())
#     def __str__(self):
#         return 'Имя {} \t Возраст {}'.format(self.__name, self.__age)
# tom = Person('Tom', 34)
# print(tom)