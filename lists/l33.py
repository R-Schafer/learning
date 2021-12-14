# Write function that takes two lists and returns True if they have at least one common member.

def compare_lists(a, b):
    for x in a:
        if x in a and x in b:
            return True

    return False


def main():
    print(compare_lists([1, 2, 3], [4, 5, 1]))

main()