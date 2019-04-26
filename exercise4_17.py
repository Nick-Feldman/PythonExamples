'''
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).
'''

def accumulator(n):
    if n == 0:
        return 1
    else:
        return (accumulator(n-1) + 100)

num = int(input("Please enter a positive integer"))
print(accumulator(num))

