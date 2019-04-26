'''
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"]
 and the object is in ["Hockey","Football"].
'''

subject = ["I", "You"]

verb = ["Play", "Love"]

objects = ["Hockey", "Football"]

for i in subject:
    for j in verb:
        for k in objects:
            print(i + " " + j + " " + k)
            print()

