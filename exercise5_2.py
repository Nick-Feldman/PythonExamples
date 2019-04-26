numbers = [2,4,6,8]
for x in numbers:                          #this program uses assertion statements to verify even numbers are even,
    assert x % 2 == 0, "Not Even"          #I changed one number to odd and it raised AssertionError correctly.
