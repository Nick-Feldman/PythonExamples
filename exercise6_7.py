#take a string from the user and reverse it for output.
myString = input("Please enter some text: ")

myString = myString[::-1]  #slice use start : end : step so you are starting at beginning ending at end and stepping
                           #-1 or backwords once at a time.
print(myString)
