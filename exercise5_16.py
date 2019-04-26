#Please write a program that generates a 3*5*8 3D array in which each element is a random integer, print this array.
#Shuffle the elements in the 3*5*8 3D array.


import random

#jonArray = [[[random.randint(1,100)]*8]*5]*3  #only one random integer using this method

jonArray = [[[random.randint(1,15) for k in range(3)]for j in range(3)]for i in range(3)]

for i in range(len(jonArray)):
    print()
    for j in range(len(jonArray[i])):
        print(jonArray[i][j])

for i in range(len(jonArray)):
    for j in range(len(jonArray[i])):
        random.shuffle(jonArray[i][j])

print("\n\n Shuffled array:\n\n")

for i in range(len(jonArray)):
    print()
    for j in range(len(jonArray[i])):
        print(jonArray[i][j])
