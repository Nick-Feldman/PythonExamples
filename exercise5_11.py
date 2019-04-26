'''
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7, between 1 and
1000 inclusive.
'''
import random

li = []
def ranGenerator():
    for i in range(5):
        x = 1
        while not(x % 5 == 0 and x % 7 == 0):
            x = random.randint(1, 1000)
        yield x

gen = ranGenerator()

for i in gen:
    li.append(i)

print(li)
            
