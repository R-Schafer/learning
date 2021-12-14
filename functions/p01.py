def calculating_numbers(number1, number2):
    product = number1 * number2
    sum = number1 + number2

    if product > 1000:
        return sum
    else:
        return product


def test_calculating_numbers():
    assert calculating_numbers(20, 30) == 600
    assert calculating_numbers(30, 40) == 70
    assert calculating_numbers(0, 0) == 0
    print("All tests passed!")


test_calculating_numbers()
