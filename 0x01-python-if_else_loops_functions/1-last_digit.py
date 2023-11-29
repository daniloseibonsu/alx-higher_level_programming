#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = last = int(str(number)[-1:])
string = 'no last digit'
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    string = 'and is greater than 5'
elif last == 0:
    string = 'and is 0'
elif last < 6:
    string = 'and is less than 6 and not 0'
else:
    string = string
print('Last digit of', number, 'is', last, string)
