# Get the smallest number from a list

def smallest(items):
    x = items[0]
    for i in range(0, len(items)):
        if x >= items[i]:
            x = items[i]
    return x

def main():
    print(smallest([10, 8, 0, 4, -1, 2]))

main()