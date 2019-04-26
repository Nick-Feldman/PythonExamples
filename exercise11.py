numbers = input("Please enter a comma separated series of binary numbers:")

listOfStrNum = numbers.split(",")                              #This program takes in a comma seperated series of
                                                               #binary numbers from the user and then prints the ones
listOfBins = []                                                #that are divisible by five, comma separated.

listDivFive = []

listBins = []

result = ""
temp = ""
for x in listOfStrNum:
    listOfBins.append(int(x, base=2))

for x  in listOfBins:
    if x % 5 == 0:
        listDivFive.append(x)

for x in listDivFive:
    listBins.append(bin(x))

for x in listBins:
    temp = x + ", "
    result += temp[2:]

print(result[:-2])
