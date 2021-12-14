# tic tac toe 

board = [' ' for x in range(10)]

def print_board():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def insert_letter(letter, position):
    global board
    board[position] = letter

def open_space(position):
    return board[position] == ' '

def winner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)


def player_move():
    run = True
    while run:
        move = input('Please select a position to place your X (1-9):\n')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if open_space(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('That space is occupied.\n')
            else:
                print('Please type a number between 1-9.\n')
        except:
            print('Please type a number:\n')

def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letter
            if winner(board_copy, letter):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)
    return move

    
def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
    

def board_full():
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while not(board_full()): 
        # if computer wins
        if not (winner(board, 'O')):
            player_move()
            print_board()
        else:
            print("Sorry O's won this time")
            break

        # if player wins
        if not (winner(board, 'X')):
            move = comp_move()
            if move == 0:
                print('Tie game!')
            else:
                insert_letter('O', move)
                print('Computer an O in position', move, ':')
                print_board()
        else:
            print("You won!")
            break

    # if tie
    if board_full():
        print("Tie game")


main()


