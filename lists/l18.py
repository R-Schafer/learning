# find the biggest even number in a list

def biggest_even(values):
    x = values[0]
    for i in range(0, len(values)):
        if values[i] % 2 == 0:
            if x < values[i]:
                x = values[i]
    return x

def main():
    print(biggest_even([2, 4, 8, 3, 12, 21, 6, 4]))

main()