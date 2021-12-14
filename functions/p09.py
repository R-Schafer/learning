def number_sequence(number):
    str_number = str(number)
    str_reverse_number = ""

    for i in range(len(str_number) - 1, -1, -1):
        str_reverse_number = str_reverse_number + str_number[i]

    if str_reverse_number == str_number:
        return True
    else:
        return False


def test_number_sequence():
    assert number_sequence(12222221) == True
    assert number_sequence(0) == True
    assert number_sequence(122222225) == False
    print("All tests work!")


test_number_sequence()
