cur_day = 'sunday'
my_name = 'Serhii'
greeting = 'Good day {}! {} is a perfect day to learn some python.'

print('Task 1:')
print(greeting.format(my_name, cur_day.title()))

my1stName  = 'Serhii'
myLastName = 'Zubryiuk'

fullname = my1stName + ' ' + myLastName

print('\nTask 2:')
print(greeting.format(fullname, cur_day.title()))
print('My name is {1}, {0} {1}!'.format(my1stName, myLastName))

import math

print('\nTask 3:')
print('2 + 2 = ', 2 + 2)
print('2 - 2 = ', 2 - 2)
print('7 / 3 = ', 7 / 3)
print('7 // 3 = ', 7 // 3)
print('7 % 3 = ', 7 % 3)
print('2 * 2 = ', 2 * 2)
print('2 ** 3 = ', 2 ** 3)
print('pow(2, 3) = ', 2 ** 3)
print('abs(2 - 22) = ', abs(2 - 22))
print('floor(-21.32) = ', math.floor(-21.32))
print('floor(221.32) = ', math.floor(221.32))
print('ceil(-21.32) = ', math.ceil(-21.32))
print('ceil(221.32) = ', math.ceil(221.32))
