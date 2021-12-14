# tic tac toe 

board = [' ' for x in range(9)]

def print_board():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def is_winner(move):
    return (board[0] == move and board[1] == move and board[2] == move) or (board[3] == move and board[4] == move and board[5] == move) or (board[6] == move and board[7] == move and board[8] == move) or (board[0] == move and board[3] == move and board[6] == move) or (board[1] == move and board[4] == move and board[7] == move) or (board[2] == move and board[5] == move and board[8] == move) or (board[0] == move and board[4] == move and board[8] == move) or (board[2] == move and board[4] == move and board[6] == move)

def is_valid(position):
    if not position.isdigit():
        return False
        
    position = int(position)
    if position < 0 or position > 9 or board[position - 1] != " ":
        return False

    return True
    
def board_full():
    if board.count(' ') > 0:
        return False
    else:
        return True

def main():
    print("Welcome to Tic Tac Toe!")
    current_player = "X"

    while True:
        print_board()

        position = input(f"{current_player}'s turn:\n")
        if is_valid(position):
            position = int(position)
            board[position - 1] = current_player

            if is_winner(current_player):
                print(f"{current_player} won this time")
                break
            elif board_full():
                print("Tie game")
                break
            else:
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
        else:
            print("Please enter a valid position")

main()


       
