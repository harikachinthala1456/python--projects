import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a valid length.")

else:
    password = generate_password(length)

    print("Your generated password is:", password)
