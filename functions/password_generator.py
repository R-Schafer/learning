# password generator

import random

items = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")

# asking user how long they want password
def password_length():
    return int(input("How long do you want your new password?\n"))

# creating a password
def password(number):
    new_password = ""
    i = 0
    while i < number:
        new_password = new_password + random.choice(items)
        i += 1
    return new_password

def main():
    number = password_length()
    print(password(number))

main()


