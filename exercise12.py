result = ""
for x in range(1000, 3001):
    numAsStr = str(x)
    numbers = []
    allEven = True
    for y in range(0, len(numAsStr)):
        if int(numAsStr[y]) % 2:
            allEven = False
    if allEven:
        result += str(x) + ", "

print(result[:-2])

