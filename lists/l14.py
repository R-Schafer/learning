# a list with numbers - check list and see if 2 values summed equal the parameter
# ex list = [ 1, 2, 3], parameter = 4, return True 
# ex list = [ 1, 2, 3], parameter = 6, return False

def check_items(values, parameter):
    for i in range(0, len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == parameter:
                return True
    return False

def main():
    print(check_items([1, 2, 3], 4))
    print(check_items([1, 2, 3], 6))
    print(check_items([4, 2, 5], 7))
    print(check_items([4, 2, 5, 10, 3], 16))


main()