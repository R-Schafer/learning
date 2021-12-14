# dragon realm

import random
import time

def intro():
    print("""You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.""")

def cave():
    user_choice = int(input("Which cave would you like to enter, 1 or 2?\n"))
    return user_choice

def checkCave(user_choice):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    if user_choice == friendlyCave:
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


def main():

    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        intro()
        user_choice = cave()
        checkCave(user_choice)

        print('Do you want to play again? (yes or no)')
        playAgain = input()

main()

