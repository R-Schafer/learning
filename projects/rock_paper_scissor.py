# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

player1 = input("Player 1 , please enter 'rock', 'paper', or 'scissors'\n").lower()
player2 = input("Player 2, please enter 'rock', 'paper', or 'scissors'\n").lower()

if player1 == player2:
    print(f"Tie, you both played {player1}")
# code for rock
elif player1 == 'rock':
    if player2 == 'scissors':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

# code for paper
elif player1 == 'paper':
    if player2 == 'scissors':
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

# code for scissors
elif player1 == 'scissors':
    if player2 == 'paper':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")



# The way Charlie would do it
rules = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

# determining if player 1 wins
def is_player1_winner():
    if rules[player1] == player2:
        return True
    else:
        return False
        
# determining if player 2 wins
def is_player2_winner():
    if rules[player2] == player1:
        return True
    else:
        return False
        
player1 = input("Player 1 , please enter 'rock', 'paper', or 'scissors'\n").lower()
player2 = input("Player 2, please enter 'rock', 'paper', or 'scissors'\n").lower()

if is_player1_winner():
    print("Player 1 wins!")
elif is_player2_winner():
    print("Player 2 wins!")
else:
    print("Tie!")