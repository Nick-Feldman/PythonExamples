#Jonathon's code for 5-16
import random
#
# b = 0
# array1 = []
# for i in range(8):
#     b = random.randint(1, 200)
#     array1.append(b)
# array = [[i for i in array1]*5]*3
# for i in range(3):
#     for j in range(5):
#         random.shuffle(array[i][j])
#
# for i in range(len(array)):
#     print("\n")
#     for j in range(len(array[i])):
#         print(array[i][j])

#Use a list comprehension to square each odd number in a list. The list is input by a sequence of
#comma-separated numbers.
stringInput = input("Please enter a comma separated list of integers: ")

stringNumbers = stringInput.split(", ")

numbers = []

for i in stringNumbers:
    numbers.append(int(i))

squares = [x**2 for x in numbers]

print(squares)
