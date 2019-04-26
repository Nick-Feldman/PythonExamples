'''
Please write a program to print the running time of execution of "1+1" for 100 times.
'''

import timeit

start = timeit.default_timer()

for i in range(100):
    1+1

elapsed = timeit.default_timer() - start

print(elapsed)
