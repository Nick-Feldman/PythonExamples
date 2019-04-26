'''
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we
have?
'''

legs = 94
heads = 35

chickenLegs = 2 * 35  #count the number of legs accounted by the two legged animal - chickens

rabbits = int((legs - chickenLegs)/2)   #there are two additional legs on rabbits so the left over legs divided by two
                                   #will yield the number of rabbits
chickens =  heads - rabbits

result = "There are " + str(chickens) + " chickens and " + str(rabbits) + " rabbits on the farm."

print(result)
