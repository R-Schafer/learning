# finding the biggest number in the list and returning that value

def find_biggest(values):
    x = values[0]
    for i in range(0, len(values)):
        if x < values[i]:
            x = values[i]
    return x


def main():
    print(find_biggest([2, 8, 3, 10, 6]))

main()