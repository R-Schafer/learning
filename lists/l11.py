# looking at all items in list and checking to see if they are all the same

def all_same(values):
    for i in range(0, len(values) - 1):
        if values[i] != values[i + 1]:
            return False
    return True

def main():
    print(all_same([5, 5, 5, 6]))
    print(all_same([5, 5, 5, 5]))

main()