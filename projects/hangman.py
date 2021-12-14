# Hangman

# intro and getting the word/phrase
import getpass
print("Welcome to Hangman. Player 1 - Please enter a word or phrase. Player 2 - you will be guessing. \n")

while True:
        print("Enter a word or phrase:\n")
        phrase = getpass.getpass("").upper()
        if all(x.isalpha() or x.isspace() for x in phrase):
            break
        else:
            print("Enter a word with letters only:\n")


# making dashes
word_dashes = []
for i in phrase:
        if i != " ":
            word_dashes.append("-")
        else:
            word_dashes.append(" ")
print(''.join(word_dashes))  


# guessing
wrong_guesses = 0
guessed_letters = []
while wrong_guesses < 7:
    while True:
        print("Guess a letter:\n")
        guess = input().upper()
        if len(guess) > 1:
            print("One letter at a time, try again:\n")
        elif guess.isdigit():
            print("Letters only, try again")
        else:
            break
    
    # if letter not in phrase
    if guess not in guessed_letters and guess not in phrase:
        guessed_letters.append(guess)
        wrong_guesses += 1
        print("That letter is not present, please try again:\n")
    elif guess in guessed_letters:
        print("That letter has already been guessed, try again:\n")
    else: 
        # letter is in phrase
        for j in range(0, len(phrase)):
            if phrase[j] == guess:
                word_dashes[j] = phrase[j]
                        
    print(''.join(word_dashes))


    #if player wins
    if ''.join(word_dashes) == phrase:
        print("That is correct, you win!")
        break

    # wrong guesses - drawing the body
    if wrong_guesses == 1:
        print("Head O")
    elif wrong_guesses == 2:
        print("""Torso 
        O
        |""")
    elif wrong_guesses == 3:
        print("""Right arm 
        O
        |/""")
    elif wrong_guesses == 4:
        print("""Left arm 
        O
       \|/""")
    elif wrong_guesses == 5:
        print("""Right leg 
        O
       \|/
         \\""")
    elif wrong_guesses == 6:
        print("""Left leg
        O
       \|/
       / \\""")

        print(f"You lose, the word/phrase was {phrase}.")
        break


    

    