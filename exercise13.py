text = input("Please enter a string of characters to be parsed for contents:")

letters = 0
digits = 0

for x in range(0, len(text)):
    if (text[x] >= "a" and text[x] <= "z") or (text[x] >= "A" and text[x] <='Z'):
        letters += 1
    elif text[x] >= "0" and text[x] <= "9":
        digits += 1

print("LETTERS " + str(letters))
print("DIGITS " + str(digits))
