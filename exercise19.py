# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
# age and height are numbers. The tuples are input by console. The sort criteria is:
# Sort based on name
# Then sort based on age
# Then sort by score
# The priority is: name > age > score.

another = "Y"
persons = []

while another == "Y":
    name = input("Plese enter the person's name: ")
    age = int(input("Please enter the person's age: "))
    score = int(input("Please enter the person's score: "))
    another = input("Would you like to enter another record?(Y/N)")

    another = another.capitalize()
    person = (name, age, score)

    persons.append(person)

persons.sort()

print(persons)

