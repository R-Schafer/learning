# check if the 1st number in each list are the same
# ex [[1], [1, 2, 1], [1, 3]] = True

def check_item(values):
    for i in range(0, len(values) - 1):
        if values[i][0] != values[i + 1][0]:
            return False

    return True

def main():
    print(check_item([[3, 2, 1], [3, 2, 1], [3]]))
    print(check_item([[1, 3, 1], [3, 2, 3], [3]]))

main()

