# check if list is a palindrome
# ex [1, 2, 3, 2, 1], return True

def check_palindrome(values):
    j = len(values) - 1
    for i in range(0, len(values)):
        if values[i] != values[j]:
            return False
        else:
            j -= 1
    return True

def main():
    print(check_palindrome([1, 2, 3, 4, 1]))
    print(check_palindrome([1, 2, 3, 2, 1]))

main()