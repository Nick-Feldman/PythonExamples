'''
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

'''

text = input("Please enter some text to be analyzed: ")

count = dict.fromkeys(text)

for key in count:
    count[key] = 0

for x in range(len(text)):
    count[text[x]] += 1

for key in count:
    print(str(key) +"," + str(count[key]))

