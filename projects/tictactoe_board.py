# tic tac toe board

def board_dimensions():
    return int(input("How big would you like your board? (Hint, 3 = 3x3, 4 = 4x4, and so on)\n"))

def creating_board(size):
    x = 0
    while x < size:
        print(" --- " * size + "\n" + "|    " * (size + 1))
        x = x + 1
    print(" --- " * size)


def main():
    size = board_dimensions()
    creating_board(size)

main()


