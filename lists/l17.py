# check list and see if numbers go odd to even to odd
# ex [1, 6, 3, 8, 7, 10], return True
# ex [1, 3, 6, 7], return False

def check_order(values):
    for i in range(0, len(values)):
        if i % 2 == 0:
            if values[i] % 2 != 1:
                return False
        elif i % 2 == 1:
            if values[i] % 2 != 0:
                return False
    return True

def main():
    print(check_order([1, 4, 3, 6, 1, 8]))
    print(check_order([1, 4, 3, 16, 10, 7]))

main()