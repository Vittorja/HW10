import string
import keyword
users_variable = input("Enter the name of the variable : ")
invalid_variable = False
for letter in users_variable:
    if letter.isupper() or letter.isspace() or (letter in string.punctuation and letter != '_'):
        invalid_variable = True
        break
if users_variable.isdigit() or users_variable[0].isdigit() or users_variable in keyword.kwlist:
    invalid_variable = True
print(not invalid_variable)
