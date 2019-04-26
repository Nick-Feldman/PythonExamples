'''
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.
'''

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

number = int(input("Please enter a positive integer: "))

print(fibonacci(number))

#part 2
#The Fibonacci Sequence is computed based on the following formula:

#f(n)=0 if n=0
#f(n)=1 if n=1
#f(n)=f(n-1)+f(n-2) if n>1

#Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n
#input by console.

number = int(input("Please enter a positive integer: "))

numbers = [fibonacci(i) for i in range(number + 1)]

result = ""

for i in numbers:
    result += str(i) + ", "

result = result[:-2]

print(result)
