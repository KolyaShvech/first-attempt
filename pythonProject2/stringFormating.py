#print (1 + 1)
#print ("1" + "1")
#age = 23
#print ('Jack is ' + str(age) + ' years old' )
#print ('Jack is ' + str(23) + ' years old' )

#name = "Jack"
#age = "23"
#name_and_age = 'Ny name is {0}. I\'m {1} old.'.format(name, age)
#print(name_and_age)

#name_and_age = 'Ny name is {0}. I\'m {1} old.'.format("Jack", 23)
#print(name_and_age)
#name_and_age = 'Ny name is {}. I\'m {} old.'.format("Jack", 23)
#print(name_and_age)
#week_days = "There are 7 days in a week : {5}, {6}, {0}, {3}, {1}, {2}, {4}."\
#    .format("Tuesday",  "Thursday", "Friday", "Wednesday", "Saterday", "Sunday", "Monday")
#print (week_days)
#week_days = "There are 7 days in a week : {su}, {mo}, {tu}, {we}, {th}, {fr}, {sa}."\
#    .format(tu = "Tuesday",th = "Thursday",fr = "Friday", we = "Wednesday",sa =  "Saterday",su = "Sunday",mo = "Monday")
#print (week_days)



#float_result = 1000/7
#print (float_result)
#print ("The results of division is {0:1.3f}".format(float_result))\

# print(""""
#  {0:10.2f} {1:10.2f} {2:10.2f}
# {3:10.2f} {4:10.2f} {5:10.2f}
# {6:10.2f} {7:10.2f} {8:10.2f}
#""".format(1.334, 23.453, 562,78,
#           1.334, 23.453, 562,78,
#            1.334, 23.453, 562,78))


name = "Jack"
age = "23"
name_and_age = 'Ny name is {0}. I\'m {1} old.'.format(name, age)
print(name_and_age)
name_and_age = f'Ny name is {name}. I\'m {age} old.'
print(name_and_age)

print ('My name is %s. I\'m %d yers old' % (name, age))