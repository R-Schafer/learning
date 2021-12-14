# Guess the number
# The computer will think of a secret number from 1 to 20 and ask the user to guess it. 
# After each guess, the computer will tell the user whether the number is too high or too low. 
# The user wins if they can guess the number within six tries.

import random
number = random.randint(1, 20)
i = 0
print("I'm thinking of a number between 1 & 20")
while i <= 6:
    guess = int(input("Guess a number:\n"))
    if guess == number:
        print("Correct!")
        break
    elif guess < number:
        print("Higher")
    else:
        print("Lower")
    i += 1
    
    if i == 6:
        print(f"Nope, the number I was thinking of was {number}.")