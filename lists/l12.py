# checking a list of number and seeing if they are in increasing order
# if increasing - return True
# if not increasing - return False

def is_increasing(values):
    for i in range(0, len(values) - 1):
        if values[i] >= values[i + 1]:
            return False
    return True

def main():
    print(is_increasing([1, 3, 7, 6]))
    print(is_increasing([1, 3, 7, 9]))

main()