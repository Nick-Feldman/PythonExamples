'''
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of
digits only.
'''

text = input("Please enter some text: ")

words = text.split(" ")
nums = []
for i in words:
    try:
        i = (int(i))
    except:
        continue
    nums.append(str(i))

print(nums)

