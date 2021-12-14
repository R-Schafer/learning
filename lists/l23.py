# check if the 1st number in the first list, 2nd number in the 2nd list, and 3rd number
# in the 3rd list are the same
# ex [[2, 1, 1], [1, 2, 1], [1, 2, 3]] = True


def checking_item(values):
    for i in range(0, len(values) - 1):
        if values[i][i] != values[i + 1][i + 1]:
            return False
    return True

def main():
    print(checking_item([[3, 2, 1], [2, 3, 1], [1, 2, 3]]))
    print(checking_item([[3, 2, 1], [2, 0, 1], [1, 2, 3]]))
    
main()
