theList = [12, 24, 35, 70, 88, 120, 155]       #use enumerate and list comprehension to remove elements from a list.

obj1 = enumerate(theList)

newList = [ elem for count, elem in obj1 if count != 0 and count != 4 and count != 5 ]

print(newList)
