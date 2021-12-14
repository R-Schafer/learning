def fancy_print(numbers):
    result = ""

    for i in range(0, len(numbers)):
        number = numbers[i]

        if i == (len(numbers) - 1):
            result = result + str(number)
        else:
            result = result + str(number) + " | "

    return result


def test_fancy_print():
    assert fancy_print([]) == ""
    assert fancy_print([9]) == "9"
    assert fancy_print([1, 2, 3]) == "1 | 2 | 3"
    assert fancy_print([1, 2, 3, 3]) == "1 | 2 | 3 | 3"

    print("all tests passed!")


test_fancy_print()
