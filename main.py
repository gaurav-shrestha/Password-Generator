import random

# DATA list
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symb = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Main Program
print("\t!!CREATE PASSWORD!!\n")

letters = int(input("How many LETTERS do you want?\n"))
symbols = int(input("How many SYMBOLS do you want?\n"))
numbers = int(input("How many NUMBERS do you want?\n"))


password = ""

for letter in range(letters):
    password = password + random.choice(alpha)

for symbol in range(symbols):
    password = password + random.choice(symb)

for number in range(numbers):
    password = password + random.choice(num)

print(f"Here is your password: {password}")
