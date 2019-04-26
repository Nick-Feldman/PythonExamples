'''
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th, and 6th numbers
in [12,24,35,70,88,120,155].
'''

numbers = [12,24,35,70,88,120,155]

result = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

print(result)
