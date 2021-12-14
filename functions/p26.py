# cows and bulls

import random

# computer generated number
def generated_number():
    computer_number = str(random.randint(1000, 9999))
    return computer_number

# user guesses number
def user_number():
    user_guess = ""

    while True:
        user_guess = input("Guess a 4-digit number:\n")
        if len(user_guess) == 4 and user_guess.isdigit():
            break
    
    return user_guess

# comparing numbers and asking user to continue to guess
def comparing_numbers(user_guess, computer_number):
    cow_counter = 0
    bull_counter = 0
    for i in range(len(computer_number)):
        if computer_number[i] == user_guess[i]:
            cow_counter += 1
        else:
            bull_counter += 1
    return cow_counter, bull_counter


def main():
    computer_number = generated_number()
    guesses = 0
    while True:
        guesses += 1
        user_guess = user_number()
        cows, bulls = comparing_numbers(user_guess, computer_number)
        print(f"cows: {cows} bulls: {bulls}")
        
        if cows == len(computer_number):
            print(f"You win! It took you {guesses} guesses.")
            break
        
main()

