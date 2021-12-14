# checking a list to see if every other number is high and low
# ex [1, 8, 4, 10, 2, 7], return True
# ex [1, 8, 9, 10, 2, 7], return False

def checking_order(values):
    for i in range(0, len(values) - 1):
        if i % 2 == 0:
            if values[i] >= values[i + 1]:
                return False

        elif i % 2 == 1:
            if values[i] <= values[i + 1]:
                return False
    return True
    
def main():
    print(checking_order([2, 8, 3, 7, 4]))
    print(checking_order([2, 8, 10, 7, 4]))

main()