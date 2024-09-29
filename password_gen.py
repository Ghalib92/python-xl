import random
import string
def password_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the desired password length: "))
generated_password =password_generate(length)
print(f"Your generated password is: {generated_password}")