def extract_digits(number):
    str_number = str(number)
    reverse_number = ""

    for i in range(len(str_number) - 1, -1, -1):
        if i == 0:
            reverse_number = reverse_number + str_number[i]
        else:
            reverse_number = reverse_number + str_number[i] + " "

    return reverse_number


# print(extract_digits(7536))


def test_extract_digits():
    assert extract_digits(7536) == "6 3 5 7"
    print("works")


test_extract_digits()
