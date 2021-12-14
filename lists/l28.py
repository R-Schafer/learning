# Get the largest number from a list.

def largest(items):
    x = items[0]
    for i in range(0, len(items)):
        if x < items[i]:
            x = items[i]
    return x

def main():
    print(largest([2, 8, 3, 5, 4]))

main()