# a list of numbers - check list and see if 2 consecutive values sum equal the parameter
# ex list = [ 1, 2, 3], parameter = 3, return True 
# ex list = [ 1, 2, 3], parameter = 4, return False

def check_sum(values, parameter):
    for i in range(0, len(values) - 1):
        if values[i] + values[i + 1] == parameter:
            return True
    return False

def main():
    print(check_sum([1, 2, 3, 4], 7))
    print(check_sum([10, 2, 8, 4], 11))
    print(check_sum([16, 12, 3, 4], 15))

main()