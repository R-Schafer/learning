# Given a list of numbers, return True if first and last number of a list is same

# just printing
numbers = [10, 20, 30, 40, 10]

if numbers[0] == numbers[-1]:
    print("True")
else:
    print("False")


# using a function
def same_last(numbers):
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False

print(same_last([10, 20, 30, 40, 10]))


# testing the function
def same_last(numbers):
    return numbers[0] == numbers[-1]

def test_same_last():
    assert same_last([10, 20, 30, 40, 10]) == True
    assert same_last([10, 20, 30, 40, 50]) == False
    print("all works")

test_same_last()

