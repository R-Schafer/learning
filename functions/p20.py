# Given a list of numbers, iterate and print only the numbers which are divisible of 5

# just printing
numbers = [10, 20, 33, 46, 55]

for i in range(0, len(numbers)):
    if numbers[i] % 5 == 0:
        print(numbers[i])


# using a function
def multiples_5(numbers):
    new_list = []
    
    for i in range(0, len(numbers)):
        if numbers[i] % 5 == 0:
            new_list.append(numbers[i])

    return new_list

print(multiples_5([10, 20, 33, 46, 55]))


# testing a function
def multiples_5(numbers):
    new_list = []
    
    for i in range(0, len(numbers)):
        if numbers[i] % 5 == 0:
            new_list.append(numbers[i])

    return new_list

def test_multiples_5():
    assert multiples_5([10, 20, 33, 46, 55]) == [10, 20, 55]
    assert multiples_5([100]) == [100]
    print("all works")

test_multiples_5()
