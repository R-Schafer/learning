import random

width = 3
height = 4
board = [" "] * (width * height)
ships = 5

def place_ships():
    placed_ships = 0
    while placed_ships < ships:
        ship_position = random.randint(0, len(board) - 1)
        if board[ship_position] != "$":
            board[ship_position] = "$"
            placed_ships += 1

def print_board():
    for i in range(0, height):
        s = "|"
        for j in range(0, width):
            position = (i * width) + j
            if board[position] == "$":
                s += " " + "|" 
            else:
                s += board[position] + "|"  
        print(s)

def shoot(position):
    if board[position] == "$":
        board[position] = "X"
    elif board[position] == " ":
        board[position] = "O"
    
def main():
    print("Welcome to Battleship!")
    place_ships()
    
    while True:
        print_board()

        position = input(f"Enter your position (1 - {len(board)}):\n")
        if not position.isdigit():
            print("Numbers only!")
            continue
        
        position = int(position) - 1
        if position < 0 or position >= len(board):
            print(f"Numbers between 1 - {len(board)}.")
            continue

        shoot(position)

        # if all ships are found
        counter = 0
        for x in range(0, len(board)):
            if board[x] == "X":
                counter += 1

        if counter == ships:
            print("You sank all the ships!")
            break

main()