'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
'''

number = int(input("Please enter a positive single digit integer: "))

total = number + 11 * number + 111 * number + number * 1111

print("The total of " + str(number) + " + " + str(number*11) + " + " + str(number*111) + " + " + str(number*1111) +
" = " + str(total))
