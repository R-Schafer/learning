import random

width = 4
height = 3
board = [" "] * (width * height)
mines = 5

def print_board():
    position = 0

    for i in range(0, height):
        s = "|"
        for i in range(0, width):
            if board[position] == "#":
                s += " " + "|"
            else:
                s += board[position] + "|"
            position += 1  
        print(s)

def place_mines():
    mine = 0
    while mine < mines:
        planted_mines = random.randint(0, len(board) - 1)
        if board[planted_mines] == " ":
            board[planted_mines] = "#"
            mine += 1
            
def main():
    place_mines()
    
    print("Welcome to Minesweeper!")
    while True:
        print_board()
        guess = input(f"Pick a number between 1 - {len(board)}.\n")
        if not guess.isdigit():
            print("Try again")
            continue
        
        guess = int(guess) - 1
        if guess < 0 or guess >= len(board):
            print("Try again")
            continue

        if board[guess] == "#":
            board[guess] = "X"
            print_board()
            print("You lose!")
            break  

        if board[guess] == " ":
            board[guess] = "-"
            


main()