'''
By using list comprehension, please write a program to print the list after removing deleted numbers which are
divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''

numbers = [12,24,35,70,88,120,155]

result = [i for i in numbers if not(i % 5 == 0 and i % 7 == 0)]

print(result)
