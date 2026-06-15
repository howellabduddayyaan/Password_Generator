# --- Password Generator ---

import random
import string

# _________________________________________________________________________________________________

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Enter a number greater than 0")

    else:
        characters = (string.ascii_letters + string.digits + string.punctuation)
        
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

except ValueError:
    print("Enter a number")
# __________________________________________________________________________________________________