# Importing Modules
import random
import string

# DATA list
alpha = string.ascii_letters
list_alpha = list(alpha)

num = string.digits
list_num = list(num)

symb = string.punctuation
list_symb = list(symb)


# Defining function
def pw_generator():
    print("\t!!CREATE PASSWORD!!\n")

    letters = int(input("How many LETTERS do you want?\n"))
    symbols = int(input("How many SYMBOLS do you want?\n"))
    numbers = int(input("How many NUMBERS do you want?\n"))

    password_lst = []

    for letter in range(letters):
        rand_letter = random.choice(list_alpha)
        password_lst.append(rand_letter)

    for symbol in range(symbols):
        password_lst += random.choice(list_symb)

    for number in range(numbers):
        password_lst += random.choice(list_num)

    random.shuffle(password_lst)
    password = "".join(password_lst)
    print(f"PASSWORD= {password}")


# Calling function
if __name__ == "__main__":
    pw_generator()
