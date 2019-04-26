items = range(1, 11)

squareOfItems = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, items)))
print("Hello")
print(squareOfItems)

