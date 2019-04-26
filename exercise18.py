#A website requires the users to input username and password to register. Write a program to check the validity of
# password input by users.
#
# Following are the criteria for checking the password:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
#
# Your program should accept a sequence of comma separated passwords and will check them according to the above
# criteria. Passwords that match the criteria are to be printed, each separated by a comma.

stringInput = input("Please enter a comma separated list of passwords that meets the following criteria: \n"
                    "At least 1 letter between [a-z]\n"
                    "At least 1 number between [0-9]\n"
                    "At least 1 letter between [A-Z]\n"
                    "At least 1 character from [$#@]\n"
                    "Minimum length of transaction password: 6\n"
                    "Maximum length of transaction password: 12\n")
passwords = stringInput.split(", ")

result = ""
valid = []
upper = False
lower = False
num = False
special = False
length = False
for i in passwords:
    upper = False
    lower = False
    num = False
    special = False
    length = False
    for j in range(len(i)):
        if i[j] >= 'a' and i[j] <= 'z':
            lower = True
        if i[j] >= '0' and i[j] <= '9':
            num = True
        if i[j] >= 'A' and i[j] <= 'Z':
            upper = True
        if i[j] == '$' or i[j] == '#' or i[j] == '@':
            special = True
    if len(i) >= 6 and len(i) <= 12:
        length = True
    if upper and lower and num and special and length:
        valid.append(i)

for i in valid:
    result += i + ", "

result = result[:-2]


print(result)



