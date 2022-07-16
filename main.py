# Importing Modules
import random
import string

# DATA list
alpha = string.ascii_letters
list_alpha = list(alpha)

num = string.digits
list_num = list(num)


list_symb = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Main Program
print("\t!!CREATE PASSWORD!!\n")

letters = int(input("How many LETTERS do you want?\n"))
symbols = int(input("How many SYMBOLS do you want?\n"))
numbers = int(input("How many NUMBERS do you want?\n"))


password = ""

for letter in range(letters):
    password += random.choice(list_alpha)

for symbol in range(symbols):
    password += random.choice(list_symb)

for number in range(numbers):
    password += random.choice(list_num)

print(f"Here is your password: {password}")
