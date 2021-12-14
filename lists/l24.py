# check list and make sure they are increasing in consecutive order
# ex [1, 2, 3, 4, 5], return True
# ex [1, 2, 3, 5, 6], return False

def check_order(values):
    for i in range(0, len(values) - 1):
        if values[i] + 1 != values [i + 1]:
            return False
    return True

def main():
    print(check_order([1, 2, 3, 4, 5]))
    print(check_order([1, 2, 4, 5, 6]))

main()