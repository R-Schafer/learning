# Bagel deduction game - guess the 3 digit number
# "Bagels" - None of the three digits guessed is in the secret number.
# "Pico" - One of the digits is in the secret number, but the guess has the digit in the wrong place.
# "Fermi" - The guess has a correct digit in the correct place.
# ex. If the secret number is 456 and the player’s guess is 546, the clues would be “fermi pico pico.” 
# The “fermi” is from the 6 and “pico pico” are from the 4 and 5.

NUM_DIGITS = 3
MAX_GUESS = 10

# Random number is generated
def secret_number():
    import random
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum 

# clues are printed
def clues(secretNum, guess):
    output = ""
    if secretNum == guess:
        return "win"

    for x in range(0, len(secretNum)):  
        if secretNum[x] == guess[x]:
            output = output + "Fermi" + " "
    
        elif secretNum[x] in guess and secretNum[x] not in guess[x]:
            output = output + "Pico" + " "
                
    if len(output) > 0:
        return output
    else:
        return "Bagels"
    

def main():
    secretNum = secret_number()
    wrong_guesses = 0
    while wrong_guesses < MAX_GUESS:
        while True:
            guess = input("Guess a 3 digit number with 3 different numbers - DO NOT USE THE SAME NUMBER TWICE:\n")

            if not guess.isdigit():
                print("Must be numbers only.")
            elif len(guess) != 3:
                print("Must be 3 digits.")
            elif guess[0] == guess[1] or guess[0] == guess[2] or guess[1] == guess[2]:
                print("Must use 3 different numbers.")
            else:
                break

        x = clues(secretNum, guess)
        if x == "win":
            break
        else:
            print(x)
            wrong_guesses += 1

    if wrong_guesses < MAX_GUESS:
        print("You win!")
    else:
        print(f"You have used all your guesses. The correct number was {secretNum}")
       
main()

    