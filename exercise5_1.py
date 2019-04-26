number = int(input("Please enter a positive integer to find the numbers between it and zero that are divisible by both "
               "five and seven."))
result = ""
#for x in range(number + 1):
#   if x % 5 == 0 and x % 7 == 0:       #This exercise was supposed to use a generator in python come up with the
#      result += str(x) + ", "          #answer.  At first I did not understand that

#print (result[:-2])

def nextDiv(number):
    for x in range(number + 1):              #so to use a generator you apparently have to use a function that
        if x % 5 == 0 and x % 7 == 0:        #uses yield instead of return, it generates an object that contains
            yield x                          #the yielded values, which can then be iterated through once it is called

for x in nextDiv(number):                    #Here an object is created by calling on nextDiv and is iterated through
    result += str(x) + ", "

print(result[:-2])
