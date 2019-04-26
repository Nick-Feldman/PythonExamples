'''
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
'''

import random

li = []
def randomGenerator():
    for i in range(5):
        x = random.randint(100, 200)
        yield x

gen = randomGenerator()

for i in gen:
    li.append(i)

print(li)

