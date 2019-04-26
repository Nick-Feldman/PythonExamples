'''
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
'''

import random

li = []

def randomGenerator():
    for i in range(5):
        x = random.randrange(100,201,2)
        yield x

gen = randomGenerator()

for i in gen:
    li.append(i)

print(li)

