import random

height = 3
width = 3
board = [" "] * (width * height)
snake_position = 8
score = 0

def place_treat():
    global score
    while True:
        treat_position = random.randint(0, len(board) - 1)
        if board[treat_position] == " ":
            board[treat_position] = "o"
            break

def print_board():
    s = ""
    s += f'┌{"─" * (width)}┐\n'
    position = 0

    for _ in range(0, height):
        s += "|"
        for _ in range(0, width):
            s += str(board[position])
            position += 1
        s += "|\n"
    s += f'└{"─" * (width)}┘\n'
    print(s)

def move(direction):
    global snake_position
    global score

    if direction == "u" and snake_position >= width:
        board[snake_position] = " "
        snake_position -= width
        if board[snake_position] == "o":
            score += 5
            place_treat()
        board[snake_position] = "~"
        
    elif direction == "d" and snake_position < len(board) - width:
        board[snake_position] = " "
        snake_position += width
        if board[snake_position] == "o":
            score += 5
            place_treat()
        board[snake_position] = "~"
            
    elif direction == "l" and snake_position % width != 0:
        board[snake_position] = " "
        snake_position -= 1
        if board[snake_position] == "o":
            score += 5
            place_treat()
        board[snake_position] = "~"

    elif direction == "r" and (snake_position - (width - 1)) % width != 0:
        board[snake_position] = " "
        snake_position += 1
        if board[snake_position] == "o":
            score += 5   
            place_treat()
        board[snake_position] = "~"

def main():
    board[snake_position] = "~"
    print("Welcome to Snake!")
    place_treat()
    print_board()
    while True:
        direction = input("Where would you like to move? (type 'u', 'd', 'l' or 'r')\nType 'q' to quit.\n")
        if direction == "q":
            break
        move(direction)
        print(f"Score = {score}")
        print_board()   
    
main()