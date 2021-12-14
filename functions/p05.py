def first_last_same(numbers):
    if numbers == []:
        return False
    elif numbers[0] == numbers[-1]:
        return True
    else:
        return False


def test_first_last_same():
    assert first_last_same([10, 20, 30, 40, 10]) == True
    assert first_last_same([10, 20, 30, 40, 50]) == False
    assert first_last_same([10]) == True
    assert first_last_same([]) == False

    print("all tests passed!")


test_first_last_same()
