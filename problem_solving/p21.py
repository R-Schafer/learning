# user guessing a randomly generated number

import random

number = random.randint(1, 10)
print("Guess a number between 1-9:\nOr type 'exit' to quit.\n")

while True:
    user_guess = input()

    if not user_guess.isdigit():
        print("Please enter a number between 1-9:\n")
        continue
        
    user_guess = int(user_guess)
    if user_guess < 1 or user_guess > 9:
        print("Please enter a number between 1-9:\n")
        continue

    if user_guess < number:
        print("Higher.")
        continue
    
    if user_guess > number:
        print("Lower.")
        continue

    if user_guess == number:
        print("That is correct!")
        break
    
    if user_guess == 'exit':
        break


    
