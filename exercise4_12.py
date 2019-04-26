'''
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print
the company name of a given email address. Both user names and company names are composed of letters only.
'''
address = input("Please enter an email address: ")

company = address.split("@")[1]

print(company)
