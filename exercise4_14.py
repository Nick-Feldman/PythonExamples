'''
Print a unicode string "hello world".
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
'''
#Python three automatically uses unicode so this question is sort of out of date.

uniString = u'hello world'

print(uniString)

text = input("Please enter some text: ")

uniText = text.encode('utf-8')

print(uniText)
