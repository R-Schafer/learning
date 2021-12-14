# uncrackable
# https://dmoj.ca/problem/wc17c3j3
#  The password must be a string between 8 and 12 characters long (inclusive), 
# such that every character is either a lowercase letter (a  z), uppercase letter (A  Z), 
# or digit (0  9). Furthermore, it must contain at least three lowercase letters, 
# at least two uppercase letters, and at least one digit.
# ex. PassW0rd - Valid


while True:
    password = input("Enter password:\n")
    counter_upper = 0
    counter_lower = 0
    
    for i in password:
        if i == i.upper() and i.isalpha():
            counter_upper += 1
            
        elif i == i.lower() and i.isalpha():
            counter_lower += 1
 
    if counter_upper < 2 or counter_lower < 3:
        print("Password must contain at least 2 uppercase letters and 3 lowercase letters.")
                
    elif len(password) < 8 or len(password) > 12:
        print("Your password must be at least 8 characters long.")
    
    elif not password.isalnum():
        print("Password must only contain a mix of letters and numbers.")

    elif password.isupper():
        print("Password must contain a lowercase letter.")

    elif password.islower():
        print("Password must contain an uppercase letter.")

    else:
        print("Valid")
        break

