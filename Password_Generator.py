# --- Password Generator ---

import random
import string

# _________________________________________________________________________________________________

while True:
    try:
        length = int(input("Enter password length: "))

        if length > 0:
            break

        else:
            print("Enter a number greater than 0")

    except ValueError:
        print("Enter NUMBERS only")

characters = (string.ascii_letters + string.digits + string.punctuation)  

password = ""

for i in range(length):
    password += random.choice(characters)  

print("\nGenerated Password:", password)

# __________________________________________________________________________________________________