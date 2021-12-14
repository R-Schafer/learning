# Repeatedly asks users for their age and a password until they provide valid input.

while True:
    age = input("Enter your age:\n")
    if age.isdecimal():
        break

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        print("New password confirmed!")
        break