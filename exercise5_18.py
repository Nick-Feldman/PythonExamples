'''
Please write a program to print the list after removing deleteed even numbers in [5,6,77,45,22,12,24].
'''

numbers = [5,6,77,45,22,12,24]

result = []

for i in numbers:
    if i % 2 != 0:
        result.append(i)

print(result)
