'''
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is
input by console.
'''

def evenNumGens(num):
    for i in range(num + 1):
        if i % 2 == 0:
            yield i

number = int(input("Please enter a number: "))

gen = evenNumGens(number)

result = ""

for i in gen:
    result += str(i) + ", "

result = result[:-2]

print(result)

