#Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.

stringInput = ""
another = 'Y'
total = 0

while another == 'Y':
    stringInput = input("Please enter a bank transaction either D for Deposit or W for Withdrawal followed by the"
                        + "amount:\n  For example: D 100 to deposit one hundred dollars:  ")
    data = stringInput.split(" ")
    trans = data[0].capitalize()
    amount = int(data[1])
    if trans == 'D':
        total += amount
    elif trans == 'W':
        total -= amount
    else:
        print("Error inputting data!")
    another = input("Enter another transaction? (Y/N):  ")
    another = another.capitalize()

print("The total balance is now $" + str(total))

