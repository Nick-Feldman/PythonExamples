#Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

def divGenerator(n):
    for x in range(n + 1):
        if x % 7 == 0:
            yield x

number = int(input("Please enter an integer: "))

gen = divGenerator(number)

result = ""

for i in gen:
    result += str(i) + " "

print(result)
