'''
By using list comprehension, please write a program that generates a 3*5*8 3D array in which each element is 0.
'''

array = [[[0 for k in range(8)]for j in range(5)] for i in range(3)]

for i in range(len(array)):
    print("\n")
    for j in range(len(array[i])):
        print(array[i][j])


#from Jonathon --

josh = [[["Josh"]*8]*5]*3

for i in range(len(josh)):
    print("\n")
    for j in range(len(josh[i])):
        print(josh[i][j])

